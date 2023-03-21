import socket
import pandas as pd
import openpyxl

db = pd.read_excel('database.xlsx', sheet_name = 'main')
db.set_index('user id', inplace=True)

user_name = input("Enter User ID: \n")
password = input("Enter pasword: \n")

def login(id,pw):
    if id in db.index:
        if db.loc[id, 'password'] == pw:
            return True, db.loc[id]
    return False, None

def stock_balance(id):
    sheet = pd.read_excel('database.xlsx', sheet_name = id)
    print(sheet.head())

def available_stocks():
    sheet = pd.read_excel('database.xlsx', sheet_name = 'Stocks')
    print(sheet)

success, user_info = login(user_name, password)

if success:
    print(f"Logged in as user {user_info.name}")
    usd_balance = "{:.2f}".format(user_info['usd bal'])
    print(f"USD balance: ${usd_balance}")
    stock_balance(user_name)

else:
    print("Invalid login credentials")


available_stocks()
