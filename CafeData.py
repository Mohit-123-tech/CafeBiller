import random
import sqlite3
import datetime
from colorama import Fore

Menu = '''
        CODE FOR CONTINUE
        
Continue [1]
Show Data With Custommer ID [2]

'''
print(Fore.GREEN, Menu, Fore.WHITE)

def CustomerID():
    Num = "1234567890"
    Char = "@$&#"
    length = 10
    all = Num+Char

    data = "".join(random.sample(all, length))
    return data


def Bill(Name, Number, Address, Pincode, Amount, CustomerID):
    print("\n\n*********** CUSTOMER BILL ************\n\n")
    print(Fore.GREEN, f"Customer Name : {Name}")
    print(f"Customer Contact : {Number}")
    print(f"PinCode : {Pincode}")
    print(f"Full Address : {Address}")
    print(f"Bill Amount : {Amount}")
    print(f"Customer ID : {CustomerID}", Fore.WHITE)
    print(f"\n\n ***** HAPPY SHOPPING ***** ")


def DBase(Name, Number, Address, Pincode, Amount, CustomerID):
    Connection = sqlite3.connect("Database/CafeBase.db")
    Connect = Connection.cursor()
    Date = datetime.date.today()

    Connect.execute("INSERT INTO CafeBillData(Date, Name, Number, Address, Pincode, Amount, CustomerID) VALUES(?,?,?,?,?,?,?);", (Date, Name, Number, Address, Pincode, Amount, CustomerID))

    Connection.commit()
    Connection.close()


def ReadDatabase(CustomerID):
    Connection = sqlite3.connect("Database/CafeBase.db")
    Connect = Connection.cursor()

    try:
        Connect.execute(f'SELECT * FROM CafeBillData WHERE CustomerID = "{CustomerID}"')
        return Connect.fetchall()
    except(Exception):
        pass

    Connection.commit()
    Connection.close()
    
