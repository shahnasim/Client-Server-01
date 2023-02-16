import socket

def commands():
    while True:
        command = input("Enter your command (BUY, SELL, LIST, BALANCE, QUIT, SHUTDOWN): ")
        if command in ["BUY", "buy"]:
            stock_symbol = input("Enter stock symbol: \n")
            stock_amount = input("Enter stock amount: \n")
            price = input("Enter price per stock: \n")
            user_id = input("Enter user ID: \n")
            request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"
            return request
        
        elif command in ["SELL", "sell"]:
            stock_symbol = input("Enter stock symbol: \n")
            stock_amount = input("Enter stock amount: \n")
            price = input("Enter price per stock: \n")
            user_id = input("Enter user ID: \n")
            request = command + " " + stock_symbol + " " + str(stock_amount) + " " + str(price) + " " + user_id + "\n"
            return request
        
        elif command in ["LIST", "list"]:
            return command
        
        elif command in ["BALANCE", "balance"]:
            name = input("Enter user name: \n")
            request = command + " " + name + "\n"
            return request
        
        elif command in ["SHUTDOWN", "shutdown"]:
            return command
        
        elif command in ["QUIT", "quit"]:
            return command
        
        else:
            print("400 invalid command")


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_PORT = 7418 
    client.connect(('0.0.0.0', SERVER_PORT))

    while True:
        request = commands()
        client.send(request)

        response = client.recv(1024)
        print(response.decode())

        if "BALANCE" in request:
            balance_response = client.recv(1024)
            print(balance_response.decode())


if __name__ == "__main__":
    main()

