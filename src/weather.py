from typing import Protocol


class WeatherInfoBase(Protocol):
    def getWeatherInfo(self, city, country):
        ...


class WeatherInfo(WeatherInfoBase):
    def getWeatherInfo(self, city, country):
        pass
