#ATM project
from datetime import datetime
'''def bank():
    print(10*"*", "WELCOME TO THE BANK", 10*"*")
    ATMcard=input("Insert your card\n")
    Pinnumber=int(input(("Enter your Pin\n")))
bank()
def options():
    yield ("1. Withdraw Amount")
    yield ("2. Deposit Amount")
    yield ("3. Available Balance")
    yield ("4. MiniStatement")
i=options()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())  
options()
def inputs():
    options=int(input("Select your options\n"))
    if options==1:
        Available_Balance=10000
        Withdrawn=int(input("Enter amount to withdraw\n"))
        Available_Balance-=Withdrawn
        print("Total Amount withdrawn\n""Rs/-",(float(Withdrawn)),"\n",Available_Balance)
    elif options==2:
        Deposited=int(input("Enter deposit amount\n"))
        Available_Balance+=Deposited
        print("Total Amount deposited\n""Rs/-",(float(Deposited)),"\n",Available_Balance)
    elif options==3:
        print("Available Balance\n", Available_Balance)
    elif options==4:
        print(10*"-", "MiniStatement", 10*"-")
        print("Bank LTD.", 3*" ", "Gajuwaka, Visakhapatnam")
        print("Date:", datetime.now())
        print("Card number: xxxxxxxxxxxx7351")
        print("Statement print for")
        print("From A/C.")
        print("Withdrawl", (float(Withdrawn)))
        print("Credited", (float(Deposited)))
        print("Available balance:", Available_Balance)
        print(10*"-", "Thank you!", 10*"-")
        print(9*"-", "Visit Again", 9*"-")
    elif options>4:
        print("There are no options")
    else:
        print("Enter vaidate Pin")
inputs()'''


''''def bank():
    print(10*"*", "WELCOME TO THE BANK", 10*"*")
    ATMcard=input("Insert your card\n")
    Pinnumber=int(input(("Enter your Pin\n")))
bank()
def options():
    yield ("1. Withdraw Amount")
    yield ("2. Deposit Amount")
    yield ("3. Available Balance")
    yield ("4. MiniStatement")
i=options()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__()) 
Available_Balance=10000
user=int(input("Enter your options\n"))
if user==1:
    Withdrawn=int(input("Enter the amount to withdraw\n"))
    Available_Balance-=Withdrawn
    print("Amount withdrawn sucessfully\n",float(Withdrawn))
if user==2:
    Deposited=int(input("Enter the amount to deposit\n"))
    Available_Balance+=Deposited
    print("Amount deposited sucessfully\n",float(Deposited))
if user==3:
    print("Available balance\n",Available_Balance)
if user==4:
    print(10*"-", "MiniStatement", 10*"-")
    print("Bank LTD.", 3*" ", "Gajuwaka, Visakhapatnam")
    print("Date:", datetime.now())
    print("Card number: xxxxxxxxxxxx7351")
    print("Statement print for")
    print("From A/C.")
    #print("Withdrawl", float(Withdrawn))
    #print("Credited", float(Deposited))
    print("Available balance:", Available_Balance)
    print(10*"-", "Thank you!", 10*"-")
    print(9*"-", "Visit Again", 9*"-")
options()'''










print(10*"*", "WELCOME TO THE BANK", 10*"*")
ATMcard=input("Insert your card\n")
Pinnumber=int(input(("Enter your Pin\n")))
Options='''
    1. Withdraw Amount
    2. Deposit Amount
    3. Available Balance
    4. MiniStatement'''
print(Options)
user=int(input("Enter your options\n"))
def inputs():
    Available_Balance=10000
    if user==1:
        Withdrawn=int(input("Enter amount to withdraw\n"))
        Available_Balance-=Withdrawn
        print("Amount withdrawn sucessfully\n",float(Withdrawn))
    if user==2:
        Deposit=int(input("Enter amount to deposit\n"))
        Available_Balance+=Deposit
        print("Amount deposited sucessfully\n",float(Deposit))
    if user==3:
        print("Available balance\n",Available_Balance)
    if user==4:
        print("======MiniStatement======")
        print("Bank LTD.", 3*" ", "Gajuwaka, Visakhapatnam")
        print("Date:", datetime.now())
        print("Card number: xxxxxxxxxxxx7351")
        print("Statement print for")
        print("From A/C.")
        print("Available balance:", Available_Balance)
        print(10*"-", "Thank you!", 10*"-")
        print(9*"-", "Visit Again", 9*"-")
inputs()