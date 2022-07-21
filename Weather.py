import requests
import API


def get_weather(q):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": {q}, "lang": "null", "units": "metric"}

    headers = {
        "X-RapidAPI-Key": f"{API.WEATHER_KEY}",
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    try:
        return ("Current Temp: " + str(round(float(data["main"]["temp"]))) + " °C" + "\n" +
                "Feels like: " + str(round(float(data["main"]["feels_like"]))) + " °C" + "\n" +
                "Min: " + str(round(float(data["main"]["temp_min"]))) + " °C" + "\n" +
                "Max: " + str(round(float(data["main"]["temp_max"]))) + " °C")
    except:
        return "Wrong City name"
