import socket

SERVER_PORT = 12345 #REPLACE WITH UMID

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', SERVER_PORT))
server_socket.listen(1)

conn,addr = server_socket.accept()
data = conn.recv(1024).decode()
command = data.split()[0]

def user():
    
    id = 0
    balance = 0.00

def Stock():
    
    price = 0.00
    amount = 0

def processBuy():
    pass

def processSell():
    pass

def processList():
    pass

def processBalance():
    pass

def processQuit():
    pass

def processShutdown():
    pass
