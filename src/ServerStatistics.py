import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from typing import Protocol
from matplotlib import pyplot as plt


class ServerStatsProtocol(Protocol):
    def request_server_pop_plot(self, data, figure):
        ...

    def request_server_channel_pop_plot(self, data, figure):
        ...

    def request_server_pop_predictions(self, data, figure):
        ...

    def request_most_popular_members(self, data):
        ...
