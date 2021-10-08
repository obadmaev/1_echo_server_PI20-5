import socket
import threading
def read_sok():
     while True:
         data = sock.recv(1024)
         print(data.decode('utf-8'))
server = '127.0.0.1', 9091
U_Name = input("Input your name: ") #просим клиента ввести имя
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.sendto((U_Name+' Connect to server').encode('utf-8'), server)
stream = threading.Thread(target= read_sok) # вызываем функцию read_sok
stream.start()
while True:
    message = input()
    sock.sendto(('['+U_Name+']'+message).encode('utf-8'), server) #рассылка другим клиентам
