"""Creates Model"""
import pickle

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Reading the data from the dataset
df = pd.read_csv("4.1LCleaned.csv")
x = df["text"]
y = df["emotions"]

cv = CountVectorizer()

df = pd.read_csv("4.1LCleaned.csv")
print(len(df))

print(df.head())
x = df["text"]
y = df["emotions"]
cv = CountVectorizer()

x_vectorized = cv.fit_transform(x.apply(lambda x: np.str_(x)))

pickle.dump(cv, open("vectorizer.pkl", "wb"))

# Splitting the dataframe
df_split = train_test_split(x_vectorized, y, train_size=0.9, random_state=42)

x_train = df_split[0]
x_test = df_split[1]
y_train = df_split[2]
y_test = df_split[3]

# Fitting to naive
nb = MultinomialNB()
nb.fit(x_train, y_train)
accuracyNB = nb.score(x_test, y_test)
print(accuracyNB)
with open("nb.pkl", "wb") as f:
    pickle.dump(nb, f)
