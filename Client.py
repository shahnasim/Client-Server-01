import socket
def commands():
    while True:
        command = raw_input("Enter your command (BUY, SELL, LIST, BALANCE, QUIT, SHUTDOWN): ")
        if command in ["BUY", "buy"]:
            stock_symbol = raw_input("Enter stock symbol: \n")
            stock_amount = raw_input("Enter stock amount: \n")
            price = raw_input("Enter price per stock: \n")
            user_id = raw_input("Enter user ID: \n")
            request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"
            return request

        elif command in ["SELL", "sell"]:
            stock_symbol = raw_input("Enter stock symbol: \n")
            stock_amount = raw_input("Enter stock amount: \n")
            price = raw_input("Enter price per stock: \n")
            user_id = raw_input("Enter user ID: \n")
            request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"
            return request

        elif command in ["LIST", "list"]:
            return command

        elif command in ["BALANCE", "balance"]:
            balance = 0.00
            name = raw_input("Enter user name: \n")
            print("Balance for user " + name + ": $" + str(balance) + "\n")
            return command

        elif command in ["SHUTDOWN", "shutdown"]:
            return command

        elif command in ["QUIT", "quit"]:
            return command

        else:
            print("400 invalid command")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_PORT = 7418
    server_address = '0.0.0.0'  # replace with the server IP address or hostname
    server_address = '0.0.0.0' 
    client.connect((server_address, SERVER_PORT))

    while True:
        request = commands()
        client.send(request.encode())
if __name__ == "__main__":
    main()
