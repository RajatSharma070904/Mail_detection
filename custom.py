import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

class custom:
    is_legit = False

    def __init__(self, mail_text) -> bool:
        # Load the dataset
        self.df = pd.read_csv('mail_data.csv')

        # Encode labels: 'spam' -> 0, 'ham' -> 1
        self.df['Category'] = self.df['Category'].map({'spam': 0, 'ham': 1})

        # Split dataset into features and labels
        self.X = self.df['Message']
        self.Y = self.df['Category']

        # Split into training and testing sets
        X_train, X_test, Y_train, Y_test = train_test_split(
            self.X, self.Y, test_size=0.2, random_state=42
        )

        # Feature extraction using CountVectorizer (Bag of Words)
        vectorizer = CountVectorizer(stop_words='english', lowercase=True)
        X_train_vectorized = vectorizer.fit_transform(X_train)
        X_test_vectorized = vectorizer.transform(X_test)

        # Convert labels to integers
        Y_train = Y_train.astype(int)
        Y_test = Y_test.astype(int)

        # Train the model using Naive Bayes Classifier
        model = MultinomialNB()
        model.fit(X_train_vectorized, Y_train)

        # Calculate accuracy
        train_predictions = model.predict(X_train_vectorized)
        train_accuracy = accuracy_score(Y_train, train_predictions)
        print(f"Training Accuracy: {train_accuracy * 100:.2f}%")

        test_predictions = model.predict(X_test_vectorized)
        test_accuracy = accuracy_score(Y_test, test_predictions)
        print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

        # Process the input email for prediction
        input_email_vectorized = vectorizer.transform([mail_text])
        prediction = model.predict(input_email_vectorized)

        # Determine if the email is legitimate or spam
        if prediction == 1:
            print("HAM EMAIL --> Useful Email")
            self.is_legit = True
        else:
            print("SPAM EMAIL --> Unwanted Email")
            self.is_legit = False

test = custom("hello you have got a lucky draw of 10000rs send your details to this mail")
print(test)