import socket

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

def prompt():
    print('1. Login')
    print('2. Buy stock')
    print('3. Get stock price')
    print('4. Logout')
    print('5. Deposit to balance')
    print('6. Exit')

def login(conn):
    id = raw_input('Enter user ID: ')
    pw = raw_input('Enter password: ')
    conn.sendall('login,%s,%s' % (id, pw))
    data = conn.recv(BUFFER_SIZE)
    print (data)

def buy_stock(conn):
    symbol = raw_input('Enter stock symbol: ')
    quantity = int(raw_input('Enter quantity: '))
    conn.sendall('buy,%s,%s' % (symbol, quantity))
    data = conn.recv(BUFFER_SIZE)
    print (data)

def get_stock_price(conn):
    symbol = raw_input('Enter stock symbol: ')
    conn.sendall('price,%s' % symbol)
    data = conn.recv(BUFFER_SIZE)
    print (data)

def logout(conn):
    conn.sendall('logout')
    data = conn.recv(BUFFER_SIZE)
    print (data)

def deposit(conn):
    amount = float(raw_input('Enter amount: '))
    conn.sendall('deposit,%.2f' % amount)
    data = conn.recv(BUFFER_SIZE)
    print (data)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('Connected to server on %s:%d' % (HOST, PORT))
    while True:
        prompt()
        choice = raw_input('Enter choice: ')
        if choice == '1':
            login(s)
        elif choice == '2':
            buy_stock(s)
        elif choice == '3':
            get_stock_price(s)
        elif choice == '4':
            logout(s)
        elif choice == '5':
            deposit(s)
        elif choice == '6':
            s.close()
            break
        else:
            print('Invalid choice. Please try again.')
    s.close()


if __name__ == '__main__':
    main()


