import time
import os
import Responses

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def uptime():
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    while True:
        time.sleep(1)
        seconds += 1

        if seconds > 59:
            seconds = 0
            minutes += 1

        if minutes > 59:
            minutes = 0
            hours += 1

        if hours > 23:
            hours = 0
            days += 1

        cls()
        print(f"{Responses.bot_name} has started...")
        print(f"Uptime {days}d:{hours}h:{minutes}m:{seconds}s")

uptime()



