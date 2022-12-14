import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPID_API = os.getenv('RAPID_API')


def get_weather(q):

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": {q}}

    headers = {
        "X-RapidAPI-Key": f"{RAPID_API}",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()


    try:
        return ("Current Temp: " + str(round(float(data['current']['temp_c']))) + " °C" + "\n" +
                "Feels like: " + str(round(float(data['current']['feelslike_c']))) + " °C" + "\n" +
                "Condition: " + str(data['current']['condition']['text']))

    except:
        return "Wrong City name"



