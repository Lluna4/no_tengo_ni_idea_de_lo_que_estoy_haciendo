import socket
import threading
import os
archivos = list(os.listdir("test2"))
EADER = 64
PORT = 5066
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
num = 0
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
path1 = ""
p1 = 1

def cli(conn, addr):
    global path1
    global num
    global p1
    num = 0
    conn.send("Archivos disponibles:".encode(FORMAT))

    for i in archivos:
        num += 1
        conn.send(f"\n{num} {i}".encode(FORMAT))
    
    archivo = conn.recv(1024).decode(FORMAT)

    try:
        p1 = archivos[int(archivo) - 1]
        path1 = ""
    except Exception:
        conn.send("ERROR".encode(FORMAT))
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    
        
    with open(f"test2/{p1}", "rb") as tt:
        data = tt.read(1024)
        while data:
            print("enviando")
            conn.send(data)
            data = tt.read(1024)

        conn.send(b"done")
    quit()


def start():
    server.listen()
    
    print(f"El servidor acepta nuevas conexiones en {SERVER}")
    while True:
        conn, addr = server.accept()
        x2 = threading.Thread(target=cli, args=(conn, addr))
        x2.start()

print("El servidor se esta inciciando")

x1 = threading.Thread(target=start)
x1.start()