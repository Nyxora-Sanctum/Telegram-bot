import telebot

API_TOKEN = '7799286978:AAHUQKbF9jKNbjxYnPNAe3LP5CvSl8l-M7I'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to YourBot! Type /info to get more information.")


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "This is a simple Telegram bot implemented in Python.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
