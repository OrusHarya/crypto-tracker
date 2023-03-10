import telebot


def send_notify(message):
    bot = telebot.Telebot("5802182735: AAHpPGbrqy4Df5hSsB2Njv03Pib7KzwMZUI")
    bot.send_message(1798624919, message)
