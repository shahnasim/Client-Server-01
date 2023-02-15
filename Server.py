import socket

class User:
    def __init__(self, email, fName, lName):
        self.email = email
        self.fName = fName
        self.lName = lName
        self.balance = 0.0

class Stock:
    def __init__(self, symbol, stockPrice, stockAmount):
        self.symbol = symbol
        self.stockPrice = stockPrice
        self.stockAmount = stockAmount

def processBuy(users, stocks, userId, stockPrice, stockAmount, symbol):
    for user in users:
        if user.email == userId:
            totalPrice = stockPrice * stockAmount
            if user.balance < totalPrice:
                print("not enough balance")
                return
            stockExists = False
            for stock in stocks:
                if stock.symbol == symbol:
                    stock.stockAmount += stockAmount
                    stockExists = True
                    break
            if not stockExists:
                stocks.append(Stock(symbol,stockPrice,stockAmount))
            print("200 OK " + str(user.balance) + " " + str(stockAmount * stockPrice))
            return
    print("User not found")

def processSell(users, stocks, userId, stockPrice, stockAmount, symbol):
    for user in users:
        if user.email == userId:
            stockExists = False
            for stock in stocks:
                if stock.symbol == symbol:
                    if stock.stockAmount < stockAmount:
                        print("Not enough stocks")
                        return
                    stock.stockAmount -= stockAmount
                    user.balance += stockPrice * stockAmount
                    stockExists = True
                    break
            if not stockExists:
                print("Stock not found")
                return
            print("200 OK " + str(user.balance) + " " + str(stockAmount * stockPrice))
            return
    print("User not found")

def processList(stocks):
    for stock in stocks:
        print(stock.symbol, stock.stockPrice, stock.stockAmount)

def processBalance(users, userId, conn):
    for user in users:
        if user.email == userId:
            conn.send(("Balance for user " + user.fName + " " + user.lName + ": $" + str(user.balance)).encode())
            return
    conn.send("User not found".encode())

def processShutdown(server):
    server.close()

def option(data, users, stocks, conn):
    #Takes the client input and compares first two letters
    if data.split()[0].upper() == "BU":
        processBuy(users, stocks, data.split()[4], float(data.split()[3]), int(data.split()[2]), data.split()[1])
    elif data.split()[0].upper() == "SE":
        processSell(users, stocks, data.split()[4], float(data.split()[3]), int(data.split()[2]), data.split()[1])
    elif data.split()[0].upper() == "LI":
        processList(stocks)
    elif data.split()[0].upper() == "BA":
        processBalance(users, data.split()[1], conn)
    elif data.split()[0].upper() == "SH":
        processShutdown(server)
    else:
        print("Invalid command")

def main():
    # Define user credentials
    users = [User("nickazzouz1520@gmail.com", "Nicholas", "Azzouz")]
    # Define stocks
    stocks = []

    # Establishing Connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_PORT = 7418
    server.bind(('0.0.0.0', SERVER_PORT))
    server.listen(1)
    conn, addr = server.accept()
    data = conn.recv(4096)
    option(data, users, stocks, conn)

if __name__ == "__main__":
    main()


