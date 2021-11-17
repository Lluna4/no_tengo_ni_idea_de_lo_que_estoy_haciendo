
import socket
import threading
import time

#import telebot
#import network
num = 0

#bot = telebot.TeleBot("1695155940:AAGntm1f5wrH7fM4N6JVWSrD552xekryTDs", parse_mode=None)


HEADER = 64
PORT = 5066
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
corriendo = True

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)
conectado = True

print(cliente.recv(1024).decode(FORMAT))
print(cliente.recv(1024).decode(FORMAT))
print(cliente.recv(1024).decode(FORMAT))
aa = input("")
cliente.send(aa.encode(FORMAT))





with open("test2.mp4", "wb") as t1:


    while True:
        print("recibiendo")
        data = cliente.recv(1024)
        if data == b"done":
            print("se acabó")
            break
        t1.write(data)
    quit()

