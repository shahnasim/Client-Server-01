import socket

def main():
    command = ["BUY", "SELL", "LIST", "BALANCE", "QUIT", "SHUTDOWN"]
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

    def processQuit():
        pass

    def processShutdown():
        pass

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 8080))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:
            data = conn.recv(4096)
            if not data: break
            from_client += data
            print (from_client)
            conn.send("I am SERVER\n")
        conn.close()
        print ('client disconnected')


if __name__ == "__main__": 
    main()
