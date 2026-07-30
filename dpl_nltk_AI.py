
# NLP USING NLTK - ALL TOPICS IN ONE PROGRAM
# 1. INTRODUCTION TO NLP (NLTK)
# Definition: NLP enables computers to understand and process human language.

# 2. TEXT MINING USING NLP
# Definition: Extracts useful information and patterns from text data.

# 3. TOKENIZATION
# Definition: Splits text into words or sentences called tokens.

# Command:
# nltk.word_tokenize(text)

# 4. STEMMING
# Definition: Reduces words to their root form by removing suffixes.

# Command:
# PorterStemmer().stem(word)

# 5. LEMMATIZATION
# Definition: Converts words to their dictionary root form.

# Command:
# WordNetLemmatizer().lemmatize(word)

# 6. POS TAGGING
# Definition: Identifies the grammatical role of each word.

# Command:
# nltk.pos_tag(tokens)

# 7. SYNTAX ANALYSIS
# Definition: Analyzes sentence structure using grammar rules.

# Command:
# RegexpParser(grammar)

# 8. CHUNKING
# Definition: Groups related words into meaningful phrases.

# Command:
# parser.parse(pos_tags)

# 9. MACHINE LEARNING + NLP
# Definition: Uses machine learning to solve text-based problems.

# INSTALL COMMANDS:
# pip install nltk scikit-learn

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.chunk import RegexpParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# DOWNLOAD REQUIRED NLTK DATA (RUN ONCE)

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


# SAMPLE TEXT

text = "Karthi is learning Natural Language Processing using Python."

print("="*60)
print("1. INTRODUCTION TO NLP (NLTK)")
print("="*60)

print("Original Text:")
print(text)


# 2. TEXT MINING USING NLP

print("\n" + "="*60)
print("2. TEXT MINING USING NLP")
print("="*60)

tokens = word_tokenize(text)
print("Words Extracted:")
print(tokens)


# 3. TOKENIZATION

print("\n" + "="*60)
print("3. TOKENIZATION")
print("="*60)

print("Tokenized Words:")
print(tokens)


# 4. STEMMING

print("\n" + "="*60)
print("4. STEMMING")
print("="*60)

ps = PorterStemmer()

for word in tokens:
    print(word, "->", ps.stem(word))


# 5. LEMMATIZATION

print("\n" + "="*60)
print("5. LEMMATIZATION")
print("="*60)

lemmatizer = WordNetLemmatizer()

for word in tokens:
    print(word, "->", lemmatizer.lemmatize(word))


# 6. PART OF SPEECH (POS) TAGGING

print("\n" + "="*60)
print("6. POS TAGGING")
print("="*60)

pos_tags = pos_tag(tokens)

for word, tag in pos_tags:
    print(word, ":", tag)


# 7. SYNTAX ANALYSIS

print("\n" + "="*60)
print("7. SYNTAX ANALYSIS")
print("="*60)

grammar = r"""
NP: {<DT>?<JJ>*<NN>}
"""

parser = RegexpParser(grammar)

tree = parser.parse(pos_tags)

print(tree)


# 8. CHUNKING

print("\n" + "="*60)
print("8. CHUNKING")
print("="*60)

chunk_grammar = r"""
NP: {<DT>?<JJ>*<NN>}
"""

chunk_parser = RegexpParser(chunk_grammar)

chunk_result = chunk_parser.parse(pos_tags)

print(chunk_result)


# 9. MACHINE LEARNING + NLP
# SENTIMENT ANALYSIS

print("\n" + "="*60)
print("9. MACHINE LEARNING + NLP")
print("="*60)

documents = [
    "I love Python",
    "Python is amazing",
    "I hate bugs",
    "This program is bad"
]

labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

model = MultinomialNB()

model.fit(X, labels)

test = ["Python is good"]

test_data = vectorizer.transform(test)

prediction = model.predict(test_data)

print("Sentence :", test[0])
print("Prediction :", prediction[0])

print("\nProgram Completed Successfully")




# Multi 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("adult.csv")

# Remove missing values
df = df.replace(' ?', pd.NA)
df = df.dropna()

# Encode categorical columns
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop('income', axis=1)  # change column name if needed
y = df['income']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

mlp = MLPClassifier(
    hidden_layer_sizes=(64,32),
    activation='relu',
    solver='adam',
    max_iter=500,
    random_state=42
)

mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)

print("MLP Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))



""" slp_acc = accuracy_score(y_test, slp.predict(X_test))
mlp_acc = accuracy_score(y_test, mlp.predict(X_test))

print("\nModel Comparison")
print("-"*30)
print(f"Single Layer Perceptron : {slp_acc:.4f}")
print(f"Multi Layer Perceptron  : {mlp_acc:.4f}") """





# Single


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("adult.csv")

# Remove missing values
df = df.replace(' ?', pd.NA)
df = df.dropna()

# Encode categorical columns
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop('income', axis=1)  # change column name if needed
y = df['income']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
) 
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, classification_report

slp = Perceptron(
    max_iter=1000,
    random_state=42
)

slp.fit(X_train, y_train)

y_pred = slp.predict(X_test)

print("SLP Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))