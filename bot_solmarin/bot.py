# -*- coding: utf-8 -*-
import telebot
import random
global respuesta
respuesta = False
bot = telebot.TeleBot("961311462:AAHxlkA4pjGnQrc2faCXdYCmGQo4tvOjJk0")
@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    global respuesta
    respuesta = True
    bot.reply_to(message, "Hola! Queria preguntarte.. conoces a LLuc? si/no")

@bot.message_handler(commands=['random'])
def photoRandom(message):
    i = (random.randint(1,5))
    switcher = {
        1: bot.send_photo(message.chat.id,open('imagenes/1.png', 'rb')),
        2: bot.send_photo(message.chat.id,open('imagenes/2.png', 'rb')),
        3: bot.send_photo(message.chat.id,open('imagenes/3.png', 'rb')),
        4: bot.send_photo(message.chat.id,open('imagenes/4.png', 'rb')),
        5: bot.send_photo(message.chat.id,open('imagenes/5.png', 'rb'))
    }
    bot.reply_to(message,switcher.get(i,"PROBLEM RANDOM"))

@bot.message_handler(content_types=['text'])
def respostas(message):
    global respuesta
    if respuesta:
        if message.text == "si":
            respuesta = False
            bot.send_message(message.chat.id,"Si? Felicidades, ya puedes decir que conoces las respuestas a todo!")
        elif message.text == "no":
            respuesta = False
            bot.send_message(message.chat.id,"En serio? Entonces no sabes lo que es la belleza.")
        else:
            respuesta = False
            bot.send_message(message.chat.id,"No entiendo tu respuesta, mira esto:")




bot.polling(none_stop=True)
