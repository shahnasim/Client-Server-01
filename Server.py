import socket
import pandas as pd
import openpyxl

def processBuy(users, stocks, stock, price, amount, user):
    if stock not in stocks:
        return "404 stock not found"
    elif users[user] < price * amount:
        return "401 unauthorized"
    else:
        users[user] -= price * amount
        stocks[stock] += amount
        return "200 OK"

def processSell(users, stocks, stock, price, amount, user):
    if stock not in stocks:
        return "404 stock not found"
    elif stocks[stock] < amount:
        return "403 forbidden"
    else:
        users[user] += price * amount
        stocks[stock] -= amount
        return "200 OK"

def processList(stocks):
    return "\n".join(["{}: {}".format(stock, stocks[stock]) for stock in stocks])

def processBalance(users, user):
    if user not in users:
        return "404 user not found"
    else:
        return "%.2f" % users[user]

def processShutdown(server):
    server.close()
    return "200 OK"

def option(data, users, stocks, conn, server):
    # Takes the client input and compares first two letters
    command = data.split()[0].upper()
    if command == "BU":
        response = processBuy(users, stocks, data.split()[1], float(data.split()[2]), int(data.split()[3]), data.split()[4])
    elif command == "SE":
        response = processSell(users, stocks, data.split()[1], float(data.split()[2]), int(data.split()[3]), data.split()[4])
    elif command == "LI":
        response = processList(stocks)
    elif command == "BA":
        response = processBalance(users, data.split()[1])
    elif command == "SH":
        response = processShutdown(server)
    else:
        response = "400 invalid command"
    return response

def main():
    # Define available stocks
    stocks = {
        'AAPL': 100,
        'GOOGL': 50,
        'AMZN': 200,
        'FB': 75,
        'MSFT': 150
    }

    # Define user data
    users = {
        '1': 1000.00,
        '2': 5000.00,
        '3': 300.00
    }

    # Create socket for server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_PORT = 7418
    server.bind(('0.0.0.0', SERVER_PORT))
    server.listen(1)
    print ("Server started and listening on port " + str(SERVER_PORT))

    while True:
        # Wait for a client connection
        conn, addr = server.accept()
        print ("Client connected from " + str(addr))

        # Process client input
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response = option(data.strip(), users, stocks, conn, server)
            conn.sendall(response)

        # Close client connection
        conn.close()

if __name__ == "__main__":
    main()