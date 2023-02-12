import socket

def main():

    def commands():
        while True:
            command = raw_input("Enter your command (BUY, SELL, LIST, BALANCE, QUIT, SHUTDOWN): ")
            client.send(command)
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
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 8080))
    client.send(commands())
    from_server = client.recv(4096)
    client.close()
    print (from_server)


if __name__ == "__main__":
    main()
