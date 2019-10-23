# -*- coding: utf-8 -*-

import telebot
respuesta = False
bot = telebot.TeleBot("961311462:AAHxlkA4pjGnQrc2faCXdYCmGQo4tvOjJk0")

print respuesta
@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Queria preguntarte.. conoces a LLuc? si/no")
    respuesta = True
print respuesta
@bot.message_handler(content_types=['text'])
def respostas(message,respuesta=respuesta):
    if respuesta:
        if message.text == "si":
            respuesta = False
            bot.send_message("Si? Felicidades, ya puedes decir que conoces las respuestas a todo!")

        elif message.text == "no":
            respuesta = False
            bot.send_message("En serio? Entonces no sabes lo que es la belleza.")
        else:
            respuesta = False
            bot.send_message("No entiendo tu respuesta, mira esto:")


bot.polling(none_stop=True)
