"""Loads and returns the predictions for given message"""
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


class EmotionDetection:
    """Loads and returns the predictions for the given message"""

    def __init__(self):
        self.model = pickle.load(open("./nb.pkl", "rb"))

    def message(self, message):
        """returns the prediction for the given message"""
        x = message
        return self.model.predict(x)


if __name__ == "__main__":
    edo = EmotionDetection()
    print(edo.message("Wow, this is very nice"))
    print(edo.message("This is so sad"))
