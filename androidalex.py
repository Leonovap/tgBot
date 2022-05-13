from cgitb import html
from email import message
from re import A
import telebot

bot = telebot.TeleBot('5266660260:AAFyIXfsv-MosXXPmsECtI8kt95fq-9Iyn0')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('wepb/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)


bot.send_message(message.chat.id, 'Welcome to the club buddy!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
