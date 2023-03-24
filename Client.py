import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    action = raw_input("Enter 'login' to log in: ")
    if action == 'login':
        id = raw_input("Enter your ID: ")
        pw = raw_input("Enter your password: ")
        s.sendall('{},{},{}'.format(action, id, pw).encode())
        data = s.recv(BUFFER_SIZE).decode()
        print(data)
    else:
        print("Invalid action. Please enter 'login'.")
s.close()














