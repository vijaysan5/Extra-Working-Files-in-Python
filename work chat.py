
import numpy as np
import random
import nltk
import json

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Training data
data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hello", "Hi", "Hey", "Good morning"],
            "responses": ["Hello!", "Hi there!", "How can I help you?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "Goodbye", "See you"],
            "responses": ["Goodbye!", "See you again!"]
        },
        {
            "tag": "name",
            "patterns": ["What is your name?", "Who are you?"],
            "responses": ["I am an ANN chatbot."]
        },
        {
            "tag": "thanks",
            "patterns": ["Thank you", "Thanks"],
            "responses": ["You're welcome!", "Happy to help!"]
        },
        {
            "tag": "help",
            "patterns": ["Can you help me?", "I need help"],
            "responses": ["Sure! How can I assist you?"]
        }
    ]
}

words = []
classes = []
documents = []

# Preprocessing
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())
        words.extend(tokens)
        documents.append((tokens, intent["tag"]))

    if intent["tag"] not in classes:
        classes.append(intent["tag"])

words = [
    lemmatizer.lemmatize(w)
    for w in words
    if w.isalnum()
]

words = sorted(set(words))
classes = sorted(set(classes))

# Create training data
training = []

for doc in documents:
    bag = []

    sentence_words = [
        lemmatizer.lemmatize(w.lower())
        for w in doc[0]
    ]

    for word in words:
        bag.append(1 if word in sentence_words else 0)

    output = [0] * len(classes)
    output[classes.index(doc[1])] = 1

    training.append([bag, output])

random.shuffle(training)

X = np.array([item[0] for item in training])
Y = np.array([item[1] for item in training])

# Build ANN model
model = Sequential()

model.add(Dense(128, input_shape=(len(X[0]),), activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(len(classes), activation='softmax'))

# Compile model
model.compile(
    loss='categorical_crossentropy',
    optimizer=SGD(
        learning_rate=0.01,
        momentum=0.9,
        nesterov=True
    ),
    metrics=['accuracy']
)

# Train ANN
model.fit(X, Y, epochs=200, batch_size=5, verbose=1)

# Chatbot response function
def chatbot_response(message):

    tokens = nltk.word_tokenize(message.lower())

    tokens = [
        lemmatizer.lemmatize(w)
        for w in tokens
        if w.isalnum()
    ]

    bag = [0] * len(words)

    for w in tokens:
        if w in words:
            bag[words.index(w)] = 1

    prediction = model.predict(
        np.array([bag]), verbose=0
    )[0]

    if max(prediction) < 0.50:
        return "Sorry, I don't understand."

    index = np.argmax(prediction)
    tag = classes[index]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])


# Chat interface
print("\nANN CHATBOT")
print("Type 'quit' to exit.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(message)
    print("Bot:", response)
