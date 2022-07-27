import urllib.request, json
import os
from dotenv import load_dotenv
#import API

load_dotenv()
GIPHY_KEY = os.getenv('GIPHY_KEY')


def get_gif():
    with urllib.request.urlopen(f"https://api.giphy.com/v1/gifs/random?api_key={GIPHY_KEY}&tag=&rating=g") as url:
        data = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=True))
        return str(data["data"]["images"]["original"]["url"])


def search_gif(q):
    with urllib.request.urlopen(f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_KEY}"
                                f"&q={q}&limit=1&offset=0&rating=g&lang=en") as url:
        data = json.loads(url.read().decode())
        try:
            return str(data["data"][0]["images"]["original"]["url"])

        except:
            return "Image not found, try again"
