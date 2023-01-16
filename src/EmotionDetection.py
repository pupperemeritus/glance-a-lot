import pickle

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB


class EmotionDetection:
    def __init__(self):
        self.model = pickle.load(open("nb.pkl", "rb"))

    def message(self, message):
        return self.model.predict(message)
