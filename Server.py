import socket

def main():
    def user():
        pass

    def stock():
        pass

    def processBuy():
        pass

    def processSell():
        pass

    def processList():
        pass

    def processBalance():
        pass

    def processQuit():
        pass

    def processShutdown():
        pass
    
    def option():
        while True:
            if command == "BUY":
                processBuy()
            elif command == "SELL":
                processSell()
            elif command == "LIST":
                processList()
            elif command == "BALANCE":
                processBalance()
            elif command == "QUIT":
                processQuit()
            elif command == "SHUTDOWN":
                processShutdown()

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 8080))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:
            command = conn.recv(1234)
            data = conn.recv(4096)
            if not data: break
            from_client += data
            print (from_client)
            conn.send("I am SERVER\n")
        conn.close()
        print ('client disconnected')


if __name__ == "__main__": 
    main()


