import os
import requests

def weather_API(place, days):
    key = os.getenv("WeatherAPI")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}"
    data = requests.get(url).json()
    spfc = data["list"][8*(days-1):8*days]
    return spfc

if __name__ == "__main__":
    print(weather_API(place="Kabul" , days=2))
