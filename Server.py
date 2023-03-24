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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Server started on {}:{}'.format(HOST, PORT))

s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(BUFFER_SIZE).decode()
    action, id, pw = data.split(',')
    if action == 'login':
        success, user_id = login(id, pw)
        if success:
            conn.sendall("Login successful. Welcome back, {}!".format(user_id).encode())
        else:
            conn.sendall("Invalid login credentials. Please try again.".encode())
    else:
        conn.sendall("Invalid action. Please enter 'login'.".encode())
    conn.close()
