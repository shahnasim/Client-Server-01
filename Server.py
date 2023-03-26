import socket
import xml.etree.ElementTree as ET
import threading

HOST = ''
PORT = 5000
BUFFER_SIZE = 1024

db_file = 'database.xml'

def handle_client(conn, addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        msg = data.decode()
        args = msg.split(',')
        action = args[0]
        if action == 'login':
            id = args[1]
            pw = args[2]
            success, user_id = login(id, pw)
            if success:
                conn.sendall("Logged in as user ID %s" % user_id)
            else:
                conn.sendall("Invalid login")
        elif action == 'buy':
            user_id = args[1]
            symbol = args[2]
            quantity = int(args[3])
            success, msg = buy_stock(user_id, symbol, quantity)
            if success:
                conn.sendall(msg)
            else:
                conn.sendall("Error: " + msg)
        elif action == 'price':
            symbol = args[1]
            price = get_stock_price(symbol)
            if price is None:
                conn.sendall("Error: Invalid symbol")
            else:
                conn.sendall("Current price of %s: %.2f USD" % (symbol, price))
        else:
            conn.sendall("Invalid action. Please enter 'login', 'buy', or 'price'.")

    conn.close()

# Login the user
def login(action, id, pw):
    try:
        tree = ET.parse(db_file)
        root = tree.getroot()
        for user in root.findall('user'):
            if user.get('id') == id and user.find('password').text == pw:
                user.find('status').text = "Online"
                tree.write(db_file)
                return True, id, "Welcome, {}! You are now logged in.".format(id)
        return False, None, "Login failed. Please check your credentials and try again."
    except ValueError:
        return False, None, "Login failed. Please check your credentials and try again."


# Shows user's balance--outline
def display_balance(username):
    import xml.etree.ElementTree as ET
    
    # Parse the XML file and get the root element
    tree = ET.parse(db_file)
    root = tree.getroot()

    # Find the user element with the given username
    user = root.find(".//user[@id='{}']".format(username))

    # Get the USD balance element value for the user
    usd_balance = user.find('usdBalance').text

    # Display the USD balance for the user
    print("Your current USD balance is: {}".format(usd_balance))
    
# Show stock list
def list_stock():
    tree = ET.parse('stocksAvailable.xml')
    root = tree.getroot()
    stock_list = ""
    for stock in root.findall('stock'):
        if int(stock.find('quantity').text) != 0:
            stock_list += "{} - {} USD per share\n".format(stock.get('symbol'), stock.find('price').text)
    return stock_list

# Sell the stock
def sell_stock(user_id, symbol, quantity):
    # Load the XML files
    user_tree = ET.parse(db_file)
    user_root = user_tree.getroot()
    stock_tree = ET.parse('stocksAvailable.xml')
    stock_root = stock_tree.getroot()

    # Find the user with the given ID
    user_elem = user_root.find("./user[@id='%s']" % user_id)

    # Check if the user owns the stock, and if so, update the quantity
    stock_elem = user_elem.find("stocks/stock[@symbol='%s']" % symbol)
    if stock_elem is None:
        return False, "You don't own any shares of this stock"

    current_quantity = int(stock_elem.find('quantity').text)
    if current_quantity < quantity:
        return False, "You don't have enough shares of this stock to sell"

    # Subtract the sold quantity from the user's stock quantity
    stock_elem.find('quantity').text = str(current_quantity - quantity)

    # Update the stock's quantity and total value
    stock_info = stock_root.find("./stock[@symbol='%s']" % symbol)
    stock_info.find('quantity').text = str(int(stock_info.find('quantity').text) + quantity)
    stock_info.find('totalValue').text = str(float(stock_info.find('price').text) * int(stock_info.find('quantity').text))

    # Add the sold amount to the user's USD balance
    sold_amount = float(stock_info.find('price').text) * quantity
    user_elem.find('usdBalance').text = str(float(user_elem.find('usdBalance').text) + sold_amount)

    # Save changes to the XML files
    user_tree.write('database.xml')
    stock_tree.write('stocksAvailable.xml')

    return True, "You sold %d shares of %s for a total of %.2f USD" % (quantity, symbol, sold_amount)

# lookup
def lookup(user_id):
    tree = ET.parse(db_file)
    root = tree.getroot()
    user_elem = root.find("./user[@id='%s']" % user_id)

    if user_elem is None:
        return "User not found"

    stocks = user_elem.find("stocks")

    if stocks is None:
        return "You don't own any shares of stocks"

    stock_list = ""

    for stock in stocks.findall('stock'):
        symbol = stock.get('symbol')
        quantity = int(stock.find('quantity').text)
        if quantity == 0:
            continue
        price = get_stock_price(symbol)
        if price is None:
            continue
        total_value = price * quantity
        stock_list += "{} - {} share(s) at {} USD each, Total Value: {} USD\n".format(symbol, quantity, price, total_value)

    if stock_list == "":
        return "You don't own any shares of stocks"
    else:
        return stock_list

def shutdown():
    pass
    # chnages all users that have online status to offline status
    # and deconnects all the clints from the server

def logout():
    pass
    # changes user status to offline
    
def quit():
    pass
    # deconnects the clint from the server

def deposit(user_id, amt):
    pass
    # add the amount of money being added to the user's balance
    # save changes
    # send message back saying the deposit went throw

#
def who(user_id):
    pass
    # user_id need to equal root if the command can be run
    # print out all the user that have online statut



# Buys the stock
def buy_stock(user_id, symbol, quantity):
    # Load the XML file
    tree = ET.parse('users.xml')
    root = tree.getroot()

    # Find the user with the given ID
    user_elem = root.find("./user[@id='%s']" % user_id)

    # Check if the user has enough USD balance to buy the stock
    usd_balance = float(user_elem.find('usdBalance').text)
    stock_price = get_stock_price(symbol)
    if usd_balance < stock_price * quantity:
        return False, "Insufficient balance"

    # Subtract the purchase price from the user's USD balance
    user_elem.find('usdBalance').text = str(usd_balance - stock_price * quantity)

    # Check if the user already owns the stock, and if so, update the quantity
    stock_elem = user_elem.find("stocks/stock[@symbol='%s']" % symbol)
    if stock_elem is not None:
        stock_elem.find('quantity').text = str(int(stock_elem.find('quantity').text) + quantity)
    else:
        # Otherwise, add a new stock element for the user
        stock_elem = ET.SubElement(user_elem.find('stocks'), 'stock', {'symbol': symbol})
        quantity_elem = ET.SubElement(stock_elem, 'quantity')
        quantity_elem.text = str(quantity)

    # Save the updated XML file
    tree.write('users.xml')

    return True, "Bought %d shares of %s for %.2f USD" % (quantity, symbol, stock_price * quantity)

def get_stock_price(symbol):
    # Load the XML file
    tree = ET.parse(db_file)
    root = tree.getroot()
    for stock in root.findall('stock'):
        if stock.get('symbol') == symbol:
            return stock.find('price').text
    return 'Stock not found'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print ('Server started on {}:{}'.format(HOST, PORT))

s.listen(1)

while True:
    conn, addr = s.accept()
    print ('Connected by', addr)
    data = conn.recv(BUFFER_SIZE)
    action, id, pw = data.split(',')
    if action == 'login':
        success, user_id, msg = login('login', id, pw)
        if success:
            conn.sendall("Login successful. Welcome back, %s!" % user_id)
        else:
            conn.sendall("Invalid login credentials. Please try again.")
    elif action == 'buy':
        symbol, quantity = id, int(pw)
        success, message = buy_stock(user_id, symbol, quantity)
        if success:
            conn.sendall("Successfully bought %d shares of %s for %.2f USD" % (quantity, symbol, get_stock_price(symbol) * quantity))
        else:
            conn.sendall("Error: %s" % message)
    elif action == 'sell':
        symbol, quantiy = id, int(pw)
        success, message = sell_stock(user_id, symbol, quanity)
        if success:
            conn.sendall("Successfully solded %d shares of %s for %.2f USD" % (quantity, symbol, get_stock_price(symbol) * quantity))
        else:
            conn.sendall("Error: %s" % message)
    elif action == 'balance':
        pass
    elif action == 'lookup':
        pass
    elif action == 'deposit':
        pass
    elif action == 'list':
        pass
    elif action == 'who':
        pass
    elif action == 'logout':
        pass
    elif action == 'quit':
        pass
    elif action == 'shutdown':
        pass
    else:
        conn.sendall("Invalid action. Please enter 'login' or 'buy'.")
    conn.close()
