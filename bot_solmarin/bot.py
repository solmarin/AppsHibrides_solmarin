# -*- coding: utf-8 -*-
import telebot
import random
import os.path as path
from multiprocessing import Value
global respuesta
respuesta = False
numUsuari= Value('i',1)
bot = telebot.TeleBot("961311462:AAHxlkA4pjGnQrc2faCXdYCmGQo4tvOjJk0")
info = "MANUAL DE LAS FUNCIONES DEL BOT\n   /hola -> comienza conversación\n   /youtube -> te envia al canal\n   /random -> te envia una foto\n   /firma -> abrir archivo para firmar\n   /start o /help -> mostra manual del bot"
@bot.message_handler(commands=['start','help'])
def send_info(message):
    bot.send_message(message.chat.id, info)
@bot.message_handler(commands=['hola'])
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

@bot.message_handler(commands=['firma'])
def firma(message):
    firmado = False
    firmaUsuario = str(message.text)
    firmaUsuario= firmaUsuario.replace('/firma', '')

    if firmaUsuario == '':
        bot.reply_to(message,"No as introducido ninguna firma.")
    else:
        if path.exists('votos.txt') == True:
            f = open('votos.txt','r')
            for line in f:
                if firmaUsuario in line:
                    firmado = True
                    bot.reply_to(message,"Ya as firmado.")

            f.close()

            if not firmado:
                fic = open('votos.txt', 'a')
                fic.write(str(numUsuari.value) + " - " +firmaUsuario+"\n")
                numUsuari.value = numUsuari.value + 1
                fic.close()

        else:
            fic = open('votos.txt', 'a')
            fic.write("LLUC X PRESIDENT")
            fic.write(str(numUsuari.value) + " - " +firmaUsuario+"\n")
            numUsuari.value = numUsuari.value + 1
            fic.close()


@bot.message_handler(content_types=['text'])
def respostas(message):
    global respuesta
    if respuesta:
        if message.text == "si":
            respuesta = False
            bot.send_message(message.chat.id,"Si? Felicidades, ya puedes decir que conoces las respuestas a todo! \nPodrias firmar para que Lluc llegue a Presidente (usa el comando /firma + nom + dni)!")
        elif message.text == "no":
            respuesta = False
            bot.send_message(message.chat.id,"En serio? Entonces no sabes lo que es la belleza.")
        else:
            respuesta = False
            bot.send_message(message.chat.id,"No entiendo tu respuesta, mira esto:")
            bot.send_photo(message.chat.id,open('imagenes/5.png', 'rb'))

bot.polling(none_stop=True)
