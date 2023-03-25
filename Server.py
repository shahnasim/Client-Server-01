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
def login(id, pw):
    tree = ET.parse(db_file)
    root = tree.getroot()
    for user in root.findall('user'):
        if user.get('id') == id and user.find('password').text == pw:
            user.find('status').text = "Online"
            tree.write(db_file)
            return True, id
    return False, None

# Shows user's balance--outline
def user_balance(user_id):
    # Laod the XML file
    tree = ET.parse('users.xml')
    root = tree.getroot()
    
    # put code here
    # get the blance from user.xml for the user then send the blance over to the clinet
    
    return
    
# Show stock list
def list_stock():
    tree = ET.parse('stocksAvailable.xml')
    root = tree.getroot()
    # while or for lop that read the the stock in the stoksAvailabe.xml file'
        # if stament that cheeks to see if the quity of the file is not zero
        # if quity is not zero
            # then print out the name of the of the stock 
    return

# Sell the stock
def sell_stock(user_id, symbol, quantiry):
    tree = ET.parse('')
    root = tree.getroot()
    
    # find the user in the user.xml
    # find the stock the are selling
    # chenck if the quantiy the user what to sell is less than or equal to the amount they have
    # if do then find the stokc in the stock.xml and add the quantiry to the stock
    # and the amount with of the stock times the quantiry to the user's blance in user.xml
    # save changes to both .xml files
    # return output to clinet
    return

# lookup
def lookup(user_id):
    tree = ET.parse('')
    root = tree.getroot()
    
    #follow incrustions on the assiment pager
   return

# diff shutdown():
    # chnages all users that have online status to offline status
    # and deconnects all the clints from the server

# diff logout():
    # changes user status to offline
    
# diff quit():
    # deconnects the clint from the server

# diff deposit(user_id, amountAdded):
    # add the amount of money being added to the user's balance
    # save changes
    # send message back saying the deposit went throw

#
# diff who(user_id):
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
        success, user_id = login(id, pw)
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
            
    # elif action == 'sell':
    
    # elif action == 'blance':
    
    # elif action == 'lookup':
    
    # elif action == 'depoist':
    
    # elif action == 'list':
    
    # elif action == 'who':
    
    # elif action == 'logout':
    
    # elif action == 'quit':
    
    # elif action == 'shoutdown':
    
    
    
    
    else:
        conn.sendall("Invalid action. Please enter 'login' or 'buy'.")
    conn.close()
