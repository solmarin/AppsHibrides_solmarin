# -*- coding: utf-8 -*-
import telebot
import random
import os.path as path
from multiprocessing import Value
global respuesta
global escribiendo
escribiendo = False
respuesta = False
numUsuari= Value('i',1)
bot = telebot.TeleBot("961311462:AAHxlkA4pjGnQrc2faCXdYCmGQo4tvOjJk0")
info = "MANUAL DE LAS FUNCIONES DEL BOT\n   /hola -> comienza conversación\n   /youtube -> te envia el canal\n   /random -> te envia una foto\n   /firma + nombre + apellido + dni(12345678-A)\n   /start o /help -> mostra manual del bot"

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
    global escribiendo
    global firmado
    if escribiendo == False:
        escribiendo= True
        firmado = False
        numE = False
        i = 0
        key = message.text.split()
        dni = key[3].split('-',8);
        if len(key) < 4 or len(key[3])<9:
            bot.reply_to(message,"No as introducido una firma correcta. \nRecuerda: /firma + nombre + apellido + dni(12345678-A)")
        elif dni[0].isalpha() == True or dni[1].isdigit() == True:
                bot.reply_to(message,"No as introducido una firma correcta. \nRecuerda: el dni sigue este formato: 12345678-A")
        else:
            if path.exists('votos.txt') == True:
                f = open('votos.txt','r')
                for line in f:
                    if key[3] in line:
                        firmado = True
                        bot.reply_to(message,"Error: este dni ya esta inscrito con una firma.")
                    if str(numUsuari.value) in line:
                        numE = True
                    i+=1
                f.close()
                if numE :
                    numUsuari.value = i
                if not firmado:
                    fic = open('votos.txt', 'a')
                    fic.write(str(numUsuari.value) + " - " +key[1]+" "+key[2]+" "+key[3]+"\n")
                    bot.reply_to(message,"Gracias por tu firma! Eres el " + str(numUsuari.value)+ " que ha firmado.")
                    numUsuari.value = numUsuari.value + 1
                    fic.close()
            else:
                fic = open('votos.txt', 'a')
                fic.write("LLUC X PRESIDENT")
                fic.write(str(numUsuari.value) + " - " +key[1]+" "+key[2]+" "+key[3]+"\n")
                bot.reply_to(message,"Gracias por tu firma! Eres el "+ str(numUsuari.value) +" que ha firmado.")
                numUsuari.value = 2
                fic.close()
        escribiendo = False


    else:
        bot.send_message(message.chat.id,"En este momento no se puede acceder al archivo. Vuelve a internarlo más tarde!")
        escribiendo = False

@bot.message_handler(content_types=['text'])
def respostas(message):
    global respuesta
    if respuesta:
        if message.text == "si":
            respuesta = False
            bot.send_message(message.chat.id,"Si? Felicidades, ya puedes decir que conoces las respuestas a todo! \nPodrias firmar para que Lluc llegue a Presidente (usa el comando /firma + nombre + apellido + dni (12345678-A)!")
        elif message.text == "no":
            respuesta = False
            bot.send_message(message.chat.id,"En serio? Entonces no sabes lo que es la belleza.\nUtilitza el comando /random y ya veras... ")
        else:
            respuesta = False
            bot.send_message(message.chat.id,"No entiendo tu respuesta, mira esto:")
            bot.send_photo(message.chat.id,open('imagenes/5.png', 'rb'))

bot.polling(none_stop=True)
