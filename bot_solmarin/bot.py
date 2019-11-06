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
    imagen = ''
    i = (random.randint(1,5))
    switcher = {
        1:'imagenes/1.png',
        2:'imagenes/2.png',
        3:'imagenes/3.png',
        4:'imagenes/4.png',
        5:'imagenes/5.png',
    }

    bot.send_photo(message.chat.id,open(switcher.get(i,"PROBLEM RANDOM"), 'rb'))

@bot.message_handler(commands=['youtube'])
def youtube(message):
    bot.reply_to(message, "Aqui tienes.. el mejor canal del mundo: \n https://www.youtube.com/channel/UCgpx4FGiw485p3vujJgJ1zg")

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
            bot.send_photo(message.chat.id,open('imagenes/5.png', 'rb'))




bot.polling(none_stop=True)
