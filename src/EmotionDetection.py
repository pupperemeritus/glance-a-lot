import pickle

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB


def check_state(message: str) -> str:
    nbModel = pickle.load(open("nb.pkl", "rb"))
    state = nbModel.predict(message)
    return str(state)
