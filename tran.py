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




import tensorflow as tf
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# -----------------------------------
# Load Dataset
# -----------------------------------
data = pd.read_csv("adult.csv")

# Remove spaces from column names
data.columns = data.columns.str.strip()

# Remove leading/trailing spaces from string values
for col in data.columns:
    if data[col].dtype == object:
        data[col] = data[col].astype(str).str.strip()

# Replace ? with NaN
data.replace("?", np.nan, inplace=True)

# Remove rows containing missing values
data.dropna(inplace=True)

print("Dataset Shape:", data.shape)

# -----------------------------------
# Find Target Column Automatically
# -----------------------------------
possible_targets = [
    "income",
    "Income",
    "class",
    "Class",
    "salary",
    "Salary"
]

target = None

for col in possible_targets:
    if col in data.columns:
        target = col
        break

if target is None:
    target = data.columns[-1]

print("Target Column :", target)

# -----------------------------------
# Encode Categorical Columns
# -----------------------------------
for col in data.columns:
    if data[col].dtype == object:
        encoder = LabelEncoder()
        data[col] = encoder.fit_transform(data[col])

# -----------------------------------
# Features and Label
# -----------------------------------
X = data.drop(target, axis=1)
y = data[target]

# -----------------------------------
# Feature Scaling
# -----------------------------------
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -----------------------------------
# Train Test Split
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------
# Convert to TensorFlow Tensor
# -----------------------------------
X_train = tf.constant(X_train, dtype=tf.float32)
X_test = tf.constant(X_test, dtype=tf.float32)

y_train = tf.constant(y_train.values.reshape(-1,1), dtype=tf.float32)
y_test = tf.constant(y_test.values.reshape(-1,1), dtype=tf.float32)

# -----------------------------------
# Create Variables
# -----------------------------------
input_nodes = X_train.shape[1]

W1 = tf.Variable(tf.random.normal([input_nodes,64]))
b1 = tf.Variable(tf.zeros([64]))

W2 = tf.Variable(tf.random.normal([64,32]))
b2 = tf.Variable(tf.zeros([32]))

W3 = tf.Variable(tf.random.normal([32,1]))
b3 = tf.Variable(tf.zeros([1]))

optimizer = tf.optimizers.Adam(0.001)

# -----------------------------------
# Forward Function
# -----------------------------------
def forward(X):

    h1 = tf.nn.relu(tf.matmul(X,W1)+b1)

    h2 = tf.nn.relu(tf.matmul(h1,W2)+b2)

    output = tf.sigmoid(tf.matmul(h2,W3)+b3)

    return output

# -----------------------------------
# Training
# -----------------------------------
epochs = 20

for epoch in range(epochs):

    with tf.GradientTape() as tape:

        prediction = forward(X_train)

        loss = tf.reduce_mean(
            tf.keras.losses.binary_crossentropy(
                y_train,
                prediction
            )
        )

    variables = [W1,b1,W2,b2,W3,b3]

    gradients = tape.gradient(loss, variables)

    optimizer.apply_gradients(zip(gradients, variables))

    pred = tf.cast(prediction > 0.5, tf.float32)

    acc = tf.reduce_mean(
        tf.cast(tf.equal(pred, y_train), tf.float32)
    )

    print(f"Epoch {epoch+1:02d}  Loss={loss.numpy():.4f}  Accuracy={acc.numpy()*100:.2f}%")

# -----------------------------------
# Testing
# -----------------------------------
prediction = forward(X_test)

pred = tf.cast(prediction > 0.5, tf.float32)

test_acc = tf.reduce_mean(
    tf.cast(tf.equal(pred,y_test),tf.float32)
)

print("\nTest Accuracy :", round(test_acc.numpy()*100,2), "%")

# -----------------------------------
# Predict First Five Records
# -----------------------------------
print("\nPredictions")

result = forward(X_test[:5])

for i,p in enumerate(result):

    if p.numpy()[0] > 0.5:
        print("Person",i+1," : Income >50K")
    else:
        print("Person",i+1," : Income <=50K")












# kerat

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# -------------------------------------
# Load Dataset
# -------------------------------------
data = pd.read_csv("day.csv")

# Remove missing values
data.replace(" ?", np.nan, inplace=True)
data.dropna(inplace=True)

# -------------------------------------
# Convert Categorical Columns
# -------------------------------------
encoder = LabelEncoder()

for column in data.columns:
    if data[column].dtype == object:
        data[column] = encoder.fit_transform(data[column])

# -------------------------------------
# Features and Target
# -------------------------------------
X = data.drop("Numeric-Suffix", axis=1)      # Target column name
y = data["Numeric-Suffix"]

# -------------------------------------
# Normalize Features
# -------------------------------------
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -------------------------------------
# Split Dataset
# -------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------------
# Build Keras Model
# -------------------------------------
model = Sequential()

model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# -------------------------------------
# Compile Model
# -------------------------------------
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -------------------------------------
# Train Model
# -------------------------------------
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2
)

# -------------------------------------
# Evaluate
# -------------------------------------
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", accuracy)

# -------------------------------------
# Save Model
# -------------------------------------
model.save("adult_income_model.keras")