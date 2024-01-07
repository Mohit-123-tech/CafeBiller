# !/bin/python3

import CafeData
import os
from colorama import Fore

try:
    Code = int(input("Enter Code : "))
except(Exception):
    print("Code Not Found")
    exit()

if Code == 1:
    os.system("clear")
    Name = str(input("Customer name : ").__str__())

    while(True):
        Number = str(input("Customer Contact No. : "))

        if len(Number) > 10 or len(Number) < 10:
            print(Fore.RED, "Try Again", Fore.WHITE)
        else:
            break


    Address = str(input("Customer Address : "))

    PinCode = input("PinCode : ")

    Amount = input("Bill Amount : ")

    ID = CafeData.CustomerID()

    CafeData.Bill(Name, Number, Address, PinCode, Amount+" Rupees", ID)

    CafeData.DBase(Name, Number, Address, PinCode, Amount+" Rupees", ID)

elif Code == 2:
    os.system("clear")
    ID = input("Enter Customer ID : ")
    print(CafeData.ReadDatabase(ID))

else:
    print("No Option Found")

