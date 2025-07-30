import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from spam.preprocess import clean_text

class SpamClassifier:
    def __init__(self, model_path="model/spam_model.pkl"):
        self.model_path = model_path
        self.vectorizer = CountVectorizer()
        self.model = None

    def train(self, csv_path):
        import pandas as pd
        try:
            data = pd.read_csv(csv_path)
            texts = data['text'].apply(clean_text)
            labels = data['label']
            X = self.vectorizer.fit_transform(texts)
            self.model = MultinomialNB()
            self.model.fit(X, labels)
            with open(self.model_path, "wb") as f:
                pickle.dump((self.vectorizer, self.model), f)
            print("Model trained and saved.")
        except Exception as e:
            print(f"Error during training: {e}")

    def load(self):
        try:
            with open(self.model_path, "rb") as f:
                self.vectorizer, self.model = pickle.load(f)
            print("Model loaded successfully.")
        except FileNotFoundError:
            print("Model file not found. Please train the model first.")
            raise

    def predict(self, texts):
        for text in texts:
            cleaned = clean_text(text)
            X = self.vectorizer.transform([cleaned])
            pred = self.model.predict(X)[0]
            yield pred
