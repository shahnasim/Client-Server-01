import pandas as pd
import openpyxl

db = pd.read_excel(r'C:\Users\nicka\Desktop\PA2\database.xlsx')

db.set_index('user id', inplace=True)
def login(id,pw):
    if id in db.index:
        if db.loc[id, 'password'] == pw:
            return True, db.loc[id]
    return False, None

user_name = input("Enter User ID: \n")
password = input("Enter pasword: \n")

success, user_info = login(user_name, password)
if success:
    print(f"Logged in as user {user_info.name}")
    usd_balance = "{:.2f}".format(user_info['usd bal'])
    print(f"USD balance: ${usd_balance}")
    print(f"Stock balance: {user_info['stock bal']}")

else:
    print("Invalid login credentials")



