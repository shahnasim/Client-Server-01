import socket
import sys
import os

def main():
    # Function to define user credentials
    def user():

        global userId
        userId = server.recv()
        if userId == None:
            return("Error invalid UMID")
        userId.email = ""
        userId.fName = ""
        userId.lName = ""
        userId.passW = ""
        userId.usdBalance = 0.00
        userId.stockList = []

    # Function to get stock information
    def stock():
        global stockSymbol
        stockSymbol = server.recv().decode()
        global stockName
        stockName = server.recv().decode()
        global stockBalance
        

    #Processes BUY command
    def processBuy():
        stockAmount = server.recv().decode()
        stockPrice = server.recv().decode()
        if userId.balance < (float(stockAmount) * float(stockPrice)):
            print("not enough USD")
        else:
            userId.balance = userId.balance - (float(stockAmount) * float(stockPrice))

    #Processes SELL command
    def processSell():
        stockAmount = server.recv().decode()
        stockPrice = server.recv().decode()

    #Processes LIST command
    def processList():
        for i in userId.stockList:
            server.send(userId.stockList)

    #Processes BALANCE command
    def processBalance():
        return("balance")

    #Processes QUIT command
    def processQuit():
        server.close()

    #Processes SHUTDOWN command
    def processShutdown():
        server.close()
    
    def option():
    #Takes the client input and compares first two letters
        while True:
            if data[:2].decode("utf-8") == "BU" or "bu":
                processBuy()
            elif data[:2].decode("utf-8") == "SE" or "se":
                processSell()
            elif data[:2].decode("utf-8") == "LI" or "li":
                processList()
            elif data[:2].decode("utf-8") == "BA" or "ba":
                processBalance()
            elif data[:2].decode("utf-8") == "QU" or "qu":
                processQuit()
            elif data[:2].decode("utf-8") == "SH" or "sh":
                processShutdown()
            else:
                print("error")

    #Establishing Connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_PORT = 8080
    server.bind(('0.0.0.0', SERVER_PORT))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        while True:
            data = conn.recv(4096)
            if not data: break
            option()
        conn.close()
        print ('client disconnected')


if __name__ == "__main__": 
    main()


