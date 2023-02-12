import socket

def main():
    def user():
        pass

    def stock():
        pass

    #Processes commands
    def processBuy():
        print("buy")

    def processSell():
        print("sell")

    def processList():
        print("list")

    def processBalance():
        print("balance")

    def processQuit():
        print("quit")

    def processShutdown():
        print("shutdown")
    
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
    server.bind(('0.0.0.0', 8080))
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


