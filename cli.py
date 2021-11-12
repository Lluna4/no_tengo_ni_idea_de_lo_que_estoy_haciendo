
import socket
import threading
import time
#import telebot
#import network

#bot = telebot.TeleBot("1695155940:AAGntm1f5wrH7fM4N6JVWSrD552xekryTDs", parse_mode=None)


HEADER = 64
PORT = 5060
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!desconectar"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
corriendo = True

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)
conectado = True

with open("test2.mp4", "wb") as t1:


    while True:
        print("recibiendo")
        data = cliente.recv(1024)
        if data == b"done":
            print("se acabó")
            break
        t1.write(data)
    quit()

