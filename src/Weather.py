# import required modules
import requests
from datetime import datetime, timezone, timedelta


class OWMWeather:
    def __init__(self):
        self.api_key = "a1311da525ca1056b2960c9fb7638023"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self, city_name: str):
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city_name
        response = requests.get(complete_url)
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
            return self.data_to_string(weather_data)

        else:
            print(" City Not Found ")

    @staticmethod
    def data_to_string(data) -> str:
        res = f"""Temperature(C): {data["tempC"]}
Maximum Temperature(C): {data["temp_maxC"]}
Minimum Temperature(C): {data["temp_minC"]}
Feels Like(C): {data["feels_likeC"]}
Humidity (%): {data["humidity"]}
Description: {data["desc"]}
Cloud Cover (%): {data["cloud_cover"]}
Wind Speed (km/h): {data["wind_speed"]}
Sunrise: {datetime.fromtimestamp(data["sunrise"],tz=timezone(timedelta(hours=5,minutes=30)))}
Sunset {datetime.fromtimestamp(data["sunset"],tz=timezone(timedelta(hours=5,minutes=30)))}
City: {data["city"]}, Country: {data["country"]}"""
        return res


if __name__ == "__main__":
    wthr = OWMWeather()
    print(wthr.get_weather("Hyderabad"))
