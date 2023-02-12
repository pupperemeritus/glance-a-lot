"""Loads and returns the predictions for given message"""
import pickle


class EmotionDetection:
    """Loads and returns the predictions for the given message"""
    model = pickle.load(open("./src/nb.pkl", "rb"))

    @classmethod
    def message(cls, message):
        """returns the prediction for the given message"""
        vectorizer = pickle.load(open("./src/vectorizer.pkl", "rb"))
        vector = vectorizer.transform([message])
        return cls.model.predict(vector)


if __name__ == "__main__":
    print(EmotionDetection.message("Wow, this is very nice"))
    print(EmotionDetection.message("This is so sad"))
