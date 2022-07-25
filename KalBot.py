import telebot
import API
import Gif
import Responses as R
import Weather

bot_name = R.bot_name

TELEGRAM_KEY = API.TELEGRAM_KEY
bot = telebot.TeleBot(TELEGRAM_KEY, parse_mode=None)

print(f"{bot_name} Started...")


@bot.message_handler(commands=['start'])
def greet(message):
    photo = open(r"C:\Users\a780656\PycharmProjects\TelegramBot\Pictures\Bot Demo.png", 'rb')
    bot.send_message(message.chat.id, f"Hi {message.chat.first_name}, my name is <b>{bot_name}</b>!", parse_mode='html')
    bot.send_photo(message.chat.id, photo, caption="This is me! \nI can send Pictures!")
    bot.send_message(message.chat.id, "Use <i>/help</i> to find out what else I can do!", parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Hi I'm a <b>DEMO</b> Bot!"
                                      "\nYou can greet me and I'll <b>respond</b>."
                                      "\nYou can ask me about the <b>time</b> and the <b>date</b>."
                                      "\nYou can ask me to tell you a <b>joke</b>."
                                      "\nYou can ask for a <b>gif</b> and you will receive a random gif from the API."
                                      "\nYou can use <i>/weather</i> to get the <b>Weather</b>."
                                      "\nYou can use <i>/gif</i> to get a <b>GIF</b> from a specific category."
                                      "\nYou can also use <i>/info</i> to get more <b>information</b> about my creator.", parse_mode='html')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Hi, my name is Kaloian Kozlev and I am the creator of this bot."
                                      "\nIf you need a Bot for your social media, "
                                      "you can contact me on kbkozlev@gmail.com")


@bot.message_handler(commands=['gif'])
def gif(message):
    sent = bot.send_message(message.chat.id, "If you want a specific GIF "
                                             "\nenter <search_term>"
                                             "\nexample: cat")
    bot.register_next_step_handler(sent, condition)


def condition(message):
    q = str(message.text).lower()
    bot.send_video(message.chat.id, Gif.search_gif(q), caption=f"Here is a picture of a random {q}")


@bot.message_handler(commands=['weather'])
def weather(message):
    sent = bot.send_message(message.chat.id, "Enter City name:")
    bot.register_next_step_handler(sent, city)


def city(message):
    q = str(message.text).lower()
    bot.send_message(message.chat.id, Weather.get_weather(q))


@bot.message_handler()
def handle_message(message):
    text = str(message.text).lower()
    response = R.sample_responses(text)
    bot.send_message(message.chat.id, response)
    if "gif" in text:
        bot.send_video(message.chat.id, Gif.get_gif(), caption="I'm using an API to get this GIF")


bot.polling()
