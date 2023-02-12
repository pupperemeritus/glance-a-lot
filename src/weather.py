"""Implements the class that contains weather fetching functionality"""
from datetime import datetime, timedelta, timezone

import requests


class OWMWeather:
    """Implements weather functionality"""
    api_key = "a1311da525ca1056b2960c9fb7638023"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    @classmethod
    def get_weather(cls, city_name: str) -> str:
        """Fetches weather based on city name input"""
        complete_url = cls.base_url + "appid=" + cls.api_key + "&q=" + city_name
        try:
            response = requests.get(complete_url, timeout=1000)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                weather_data = {
                    "tempC": y["temp"] - 273,
                    "feels_likeC": y["feels_like"]-273,
                    "temp_minC": y["temp_min"]-273,
                    "temp_maxC": y["temp_max"]-273,
                    "city": x["name"],
                    "country": x["sys"]["country"],
                    "weather": x["weather"][0]["main"],
                    "desc": x["weather"][0]["description"],
                    "humidity": y["humidity"],
                    "cloud_cover": x["clouds"]["all"],
                    "wind_speed": x["wind"]["speed"],
                    "sunrise": x["sys"]["sunrise"],
                    "sunset": x["sys"]["sunset"],
                    "tz": x["timezone"]
                }
                weather_data = cls.data_to_string(weather_data)
                return weather_data
        except Exception as exc:
            print(" City Not Found ")
            print(exc)
            return exc

    @staticmethod
    def data_to_string(data) -> str:
        """Converts data to string representation"""
        tz = data["tz"]
        print(tz)
        res = f"""Temperature(C): {data["tempC"]:.2f}
Maximum Temperature(C): {data["temp_maxC"]:.2f}
Minimum Temperature(C): {data["temp_minC"]:.2f}
Feels Like(C): {data["feels_likeC"]:.2f}
Humidity (%): {data["humidity"]}
Description: {data["desc"]}
Cloud Cover (%): {data["cloud_cover"]}
Wind Speed (km/h): {data["wind_speed"]}
Sunrise: {datetime.fromtimestamp(data["sunrise"],tz=timezone(timedelta(seconds=tz)))}
Sunset {datetime.fromtimestamp(data["sunset"],tz=timezone(timedelta(seconds=tz)))}
City: {data["city"]}, Country: {data["country"]}"""
        return res


if __name__ == "__main__":
    print(OWMWeather.get_weather("Los Angeles"))
