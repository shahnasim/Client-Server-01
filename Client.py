import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    action = raw_input("Enter 'login' to log in or 'buy' to buy a stock: ")
    if action == 'login':
        id = raw_input("Enter your ID: ")
        pw = raw_input("Enter your password: ")
        s.sendall('{},{},{}'.format(action, id, pw).encode())
        data = s.recv(BUFFER_SIZE).decode()
        print(data)
    elif action == 'buy':
        user_id = raw_input("Enter your ID: ")
        symbol = raw_input("Enter the stock symbol: ")
        quantity = int(raw_input("Enter the quantity to buy: "))
        s.sendall('{},{},{},{}'.format(action, user_id, symbol, quantity).encode())
        data = s.recv(BUFFER_SIZE).decode()
        print(data)
    else:
        print("Invalid action. Please enter 'login' or 'buy'.")
s.close()











