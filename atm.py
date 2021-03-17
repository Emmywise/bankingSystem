import random

class BankAccount:
    def __init__(self):
        self.balance = 0
        print("welcome")

#function to collect customers informations
    def customer_information(self):
        global firstName
        firstName = str(input("enter your first name: "))
        global lastName
        lastName = str(input("enter your last name: "))
        global generate_accountNumber
        generate_accountNumber = random.randint(111111, 9999999)
        print("\n account number:", generate_accountNumber)


#function to deposite amount
    def deposite(self):
        amount = float(input("enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

# function to withdraw amount
    def withdraw(self):
        amount = float(input("enter amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance -= amount
            print("\n you withdraw:", amount)
        else:
            print("\n insufficient fund")

# function to display amount
    def display(self):
        print("\n full name: ", firstName +" "+ lastName )
        print("\n account number: ", generate_accountNumber)
        print ("\n total available balance: ", self.balance)

# creating an object of class
result = BankAccount()

# calling functions with that class object
result.customer_information()
result.deposite()
result.withdraw()
result.display()

       
