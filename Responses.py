import asyncio
from datetime import datetime
import random
import Jokes

bot_name = "Kaloian's Demo Bot"


def sample_responses(input_text):
    user_message = str(input_text).lower()

    user_greetings = ["hello", "hi", "sup", "hey"]
    user_feeling_good = ["good", "fine", "not bad", "nb"]
    user_feeling_bad = ["bad", "not good", "don't ask", "not very good"]
    user_thanks = ["thank you", "ty", "thanks"]
    user_ask_feeling = ["how are you", "and you", "what about you", "wbu", "hru"]
    user_ask_name = ["who are you", "what is your name", "what are you called", "who created you", "creator", "name"]
    user_ask_time = ["time", "what time is it?", "what's the time?"]
    user_ask_date = ["date", "what day is is today?", "day"]

    bot_resp_greetings = ["Hi! How are you?", "Hi!", "Sup?", "Hey, What's up?"]
    bot_resp_feel_good = ["I'm glad to hear it!", "Sounds good!", "I'm glad!", "Happy to hear it!"]
    bot_resp_feel_bad = ["Hmm... Maybe I can help?", "I'm sad to hear it!", "Maybe I can cheer you up!", "..."]
    bot_resp_thanks = ["No problem!", "I'm glad!", "Sure!"]
    bot_resp_feeling = ["I feel awesome, thank you!", "Today is a good day, I'm happy!", "I'm happy!",
                        "I'm fresh as a pickle!"]
    bot_not_understand = ["I'm not sure what you mean!", "I'm sorry I don't understand?!", "I didn't get that!",
                          "Could you try again?", "Hmm... I don't know what you mean!"]

    for i in user_greetings:
        if i in user_message:
            return random.choice(bot_resp_greetings)

    for i in user_feeling_good:
        if i in user_message:
            return random.choice(bot_resp_feel_good) + "\nWhat can I do for you?"

    for i in user_feeling_bad:
        if i in user_message:
            return random.choice(bot_resp_feel_bad) + "\nWhat can I do for you?"

    for i in user_thanks:
        if i in user_message:
            return random.choice(bot_resp_thanks)

    for i in user_ask_feeling:
        if i in user_message:
            return random.choice(bot_resp_feeling) + "\nAnd you?"

    for i in user_ask_name:
        if i in user_message:
            return f"My name is {bot_name}" + "\nMy creator is Kaloian Kozlev."

    for i in user_ask_time:
        if i in user_message:
            now = datetime.now()
            time = now.strftime("Current time: %H:%M")
            return str(time)

    for i in user_ask_date:
        if i in user_message:
            now = datetime.now()
            date = now.strftime("The date today is: %d/%m/%y")
            return str(date)

    if "help" in user_message:
        return "try /help"

    if "joke" in user_message:
        return asyncio.run(Jokes.print_joke())

    if "gif" in user_message:
        return "Thanks for asking, here you go!"

    if "weather" in user_message:
        return "Try /weather"

    return random.choice(bot_not_understand)
