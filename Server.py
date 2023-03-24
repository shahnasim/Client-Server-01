import socket
import xml.etree.ElementTree as ET

HOST = ''
PORT = 5000
BUFFER_SIZE = 1024

db_file = 'database.xml'

def login(id, pw):
    tree = ET.parse(db_file)
    root = tree.getroot()
    for user in root.findall('user'):
        if user.get('id') == id and user.find('password').text == pw:
            user.find('status').text = "Online"
            tree.write(db_file)
            return True, id
    return False, None

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
    # Replace with API call to get stock price for given symbol
    return 10.00

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
    else:
        conn.sendall("Invalid action. Please enter 'login' or 'buy'.")
    conn.close()
