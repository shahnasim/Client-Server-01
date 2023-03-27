import socket
import sys

def menu():
    print("1. Buy stock")
    print("2. Sell stock")
    print("3. Check balance")
    print("4. Deposit to balance")
    print("5. List owned stocks")
    print("6. Lookup how much of a stock you own")
    print("7. See who is connected to server")
    print("8. Logout")
    print("9. Quit")

def run():
    host = 'localhost'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    while True:
        # Ask the user whether they want to login or quit
        choice = raw_input("Enter 1 to login or 2 to quit: ")
        if choice == '2':
            s.send('quit')
            sys.exit()

        # Send the user's choice to the server
        s.send(choice)

        # If the user chose to login
        if choice == '1':
            # Ask for the username and password
            username = raw_input("Enter your username: ")
            password = raw_input("Enter your password: ")

            # Send the username and password to the server
            s.send(username)
            s.send(password)

            # Receive the server's response
            response = s.recv(1024)

            # If the login was successful
            if response == 'success':
                print("Login successful")
                while True:
                    menu()
                    # Get the user's choice
                    choice = raw_input("Enter a number: ")
                    s.send(choice)

                    # Perform the appropriate action based on the user's choice
                    if choice == '1':
                        stock = raw_input("Enter the stock name: ")
                        amount = raw_input("Enter the amount to buy: ")
                        s.send(stock)
                        s.send(amount)
                        response = s.recv(1024)
                        print(response)
                    elif choice == '2':
                        stock = raw_input("Enter the stock name: ")
                        amount = raw_input("Enter the amount to sell: ")
                        s.send(stock)
                        s.send(amount)
                        response = s.recv(1024)
                        print(response)
                    elif choice == '3':
                        s.send('check')
                        response = s.recv(1024)
                        print("Your balance is: " + response)
                    elif choice == '4':
                        amount = raw_input("Enter the amount to deposit: ")
                        s.send(amount)
                        response = s.recv(1024)
                        print(response)
                    elif choice == '5':
                        s.send('list')
                        response = s.recv(1024)
                        print(response)
                    elif choice == '6':
                        stock = raw_input("Enter the stock name: ")
                        s.send(stock)
                        response = s.recv(1024)
                        print("You own " + response + " shares of " + stock)
                    elif choice == '7':
                        s.send('connected')
                        response = s.recv(1024)
                        print(response)
                    elif choice == '8':
                        s.send('logout')
                        response = s.recv(1024)
                        if response == 'success':
                            print("Logout successful")
                            break
                    elif choice == '9':
                        s.send('quit')
                        sys.exit()

            # If the login was unsuccessful
            else:
                print("Login failed")

if __name__ == '__main__':
    run()
