import socket
import sys

SERVER_PORT = 12345

if len(sys.argv) != 2:
    print("Usage: python client.py <server_ip>")
    sys.exit(1)

server_ip = sys.argv[1]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, SERVER_PORT))

command = input("Enter the command (BUY, SELL, LIST, BALANCE, QUIT, SHUTDOWN): ")
while True:
    if command == "BUY":
        stock_symbol,user_id = ""
        stock_amount = 0
        price = 0
        input("Enter stock symbol: \n")
        input("Enter stock amount: \n")
        input("Enter price per stock: \n")
        input("Enter user ID: \n")
        request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"

    elif command == "SELL":
        stock_symbol,user_id = ""
        stock_amount = 0
        price = 0
        input("Enter stock symbol: \n")
        input("Enter stock amount: \n")
        input("Enter price per stock: \n")
        input("Enter user ID: \n")
        request = command + " "

    elif command == "LIST":
        pass

    elif command == "BALANCE":
        balance = 0.00
        name = ""
        print("Balance for user " + name + ": $" + str(balance) + "\n")

    elif command == "QUIT":
        pass

    elif command == "SHUTDOWN":
        pass

    else:
        print("Error invalid input")

    data = client_socket.recv(1024).decode()
    print("Received data: ", data)
