import pickle

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report, plot_confusion_matrix

<<<<<<< HEAD
# Reading the data from the dataset
df = pd.read_csv("4.1LCleaned.csv")
x = df["text"]
y = df["emotions"]

cv = CountVectorizer()
=======

df = pd.read_csv("4.1LCleaned.csv")
print(len(df))

df.head()
x = df["text"]
y = df["emotions"]
cv = CountVectorizer()

>>>>>>> 7224db3 (Added ML code for emotion detection)
x_vectorized = cv.fit_transform(x.apply(lambda x: np.str_(x)))

pickle.dump(cv, open("vectorizer.pkl", "wb"))

<<<<<<< HEAD
# Splitting the dataframe
=======
>>>>>>> 7224db3 (Added ML code for emotion detection)
df_split = train_test_split(x_vectorized, y, train_size=0.9, random_state=42)

x_train = df_split[0]
x_test = df_split[1]
y_train = df_split[2]
y_test = df_split[3]

<<<<<<< HEAD
# Fitting to naive bayes model
nb = MultinomialNB()

nb.fit(x_train, y_train)

accuracyNB = nb.score(x_test, y_test)

# Fitting to naive
=======
nb = MultinomialNB()
nb.fit(x_train, y_train)
nb.score(x_test, y_test)

>>>>>>> 7224db3 (Added ML code for emotion detection)
lr = LogisticRegression(max_iter=1500)
lr.fit(x_train, y_train)

pickle.dump(lr, open("lr.pkl", "wb"))
<<<<<<< HEAD

accuracyLR = lr.score(x_test, y_test)

plot_confusion_matrix(lr, x_test, y_test)
plt.show()
=======
lr.score(x_test, y_test)
plot_confusion_matrix(lr, x_test, y_test)
>>>>>>> 7224db3 (Added ML code for emotion detection)
