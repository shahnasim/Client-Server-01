import socket
import sys
import os

def main():

    def commands():
        while True:
            #Asks user what they want to do and sends command to server
            command = raw_input("Enter your command (BUY, SELL, LIST, BALANCE, QUIT, SHUTDOWN): ")
            client.send(command)

            #Sends user info to server for BUY command
            if command == "BUY":
                stock_symbol = "MSFT"
                user_id = "1234"
                stock_amount = 0
                price = 0
                stock_symbol = raw_input("Enter stock symbol: \n")
                stock_amount = raw_input("Enter stock amount: \n")
                price = raw_input("Enter price per stock: \n")
                user_id = raw_input("Enter user ID: \n")
                request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"
                client.send(request)

            #Sends user info to server for SELL command
            elif command == "SELL":
                stock_symbol = "MSFT"
                user_id = "1234"
                stock_amount = 0
                price = 0
                stock_symbol = raw_input("Enter stock symbol: \n")
                stock_amount = raw_input("Enter stock amount: \n")
                price = raw_input("Enter price per stock: \n")
                user_id = raw_input("Enter user ID: \n")
                request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"
                client.send(request)

            #Sends user info to server for LIST command
            elif command == "LIST":

                request = ""
                client.send(request)

            #Sends user info to server for BALANCE command
            elif command == "BALANCE":
                balance = 0.00
                name = ""
                print("Balance for user " + name + ": $" + str(balance) + "\n")
                request = ""
                client.send(request)

            #Sends user info to server for QUIT command
            elif command == "QUIT":

                request = ""
                client.send(request)

            #Sends user info to server for SHUTDOWN command
            elif command == "SHUTDOWN":

                request = ""
                client.send(request)

            else:
                print("Error invalid input")

    #Establishing Connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_PORT = 8080
    client.connect(('0.0.0.0', SERVER_PORT))
    client.send(commands())
    from_server = client.recv(4096)
    client.close()
    print (from_server)


if __name__ == "__main__":
    main()

