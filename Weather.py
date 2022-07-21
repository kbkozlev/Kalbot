import requests
import API


def get_weather(q):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": {q}, "lat": "0", "lon": "0", "lang": "null", "units": "metric"}

    headers = {
        "X-RapidAPI-Key": f"{API.WEATHER_KEY}",
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    try:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        return ("Current Temp: " + str(round(float(temp))) + " °C" + "\n" +
                "Feels like: " + str(round(float(feels_like))) + " °C" + "\n" +
                "Min: " + str(round(float(temp_min))) + " °C" + "\n" +
                "Max: " + str(round(float(temp_max))) + " °C")
    except:
        return "Wrong City name"
