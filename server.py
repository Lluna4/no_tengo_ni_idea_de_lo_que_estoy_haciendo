import socket
import threading

EADER = 64
PORT = 5057
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def cli(conn, addr):
    while True:
        
        
        with open("image.jpeg", "rb") as tt:
            data = tt.read(1024)
            while data:
                print("enviando")
                conn.send(data)
                data = tt.read(1024)
    
            conn.send(b"done")


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