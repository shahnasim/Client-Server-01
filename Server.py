import socket
import sys
import os

def main():
    # Function to define user credentials
    def user():
        pass

    # Function to get stock information
    def stock():
        pass

    #Processes BUY command
    def processBuy():
        print("buy")

    #Processes SELL command
    def processSell():
        return("sell")

    #Processes LIST command
    def processList():
        return("list")

    #Processes BALANCE command
    def processBalance():
        return("balance")

    #Processes QUIT command
    def processQuit():
        return("quit")

    #Processes SHUTDOWN command
    def processShutdown():
        return("shutdown")
    
    def option():
    #Takes the client input and compares first two letters
        while True:
            if data[:2].decode("utf-8") == "BU":
                processBuy()
            elif data[:2].decode("utf-8") == "SE":
                processSell()
            elif data[:2].decode("utf-8") == "LI":
                processList()
            elif data[:2].decode("utf-8") == "BA":
                processBalance()
            elif data[:2].decode("utf-8") == "QU":
                processQuit()
            elif data[:2].decode("utf-8") == "SH":
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





