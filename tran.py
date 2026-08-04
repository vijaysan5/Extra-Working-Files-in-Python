import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("adult.csv")

# Remove missing values
df.replace(" ?", pd.NA, inplace=True)
df.dropna(inplace=True)

# Encode categorical columns
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = le.fit_transform(df[col])

# Features and Target
X = df.drop("income", axis=1)      # Change if your target column has another name
y = df["income"]

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Compile Model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train Model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)

print("Accuracy:", accuracy)