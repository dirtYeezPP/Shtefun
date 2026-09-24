# PROV I OBJEKT ORIENTERING WALLAHI I EXAM SEN 

## CLASSES AND INSTANCES 

### EX. FIRST TASK -- FILMS 
class Film(): 
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating 
    def __str__(self): 
        return f"{self.title} has a rating of {self.rating}"

first_movie = Film("Spirited Away", 9.5)
second_movie = Film("Die Hard", 9)
movies = []
movies.append(first_movie)
movies.append(second_movie)

for mov in movies: 
    print(mov)

### EX. SECOND TASK -- RECTANGLE 
class Rectangle(): 
    def __init__(self, length, base):
        self.length = length 
        self.base = base 
    def area(self):
        return self.length * self.base 
    def perimeter(self):
        return 2 * self.length + 2 * self.base 
    def __str__(self): 
        return f"Rectangle length: {self.length}, and base {self.base}"

Rectangles = []
a = Rectangle(4, 5)
b = Rectangle(6, 8)
Rectangles.append(a)
Rectangles.append(b)

for r in Rectangles: 
    print(r, "area: ", r.area(), "perimeter: ", r.perimeter())

### EX. THIRD TASK -- BANK STUFF
import random

class BankCustomer(): 
    def __init__(self, name, start_saldo, reception, credit_limit = 5000):
        self.name = name
        self.start_saldo = start_saldo 
        self.reception = reception 
        self.credit_limit = credit_limit 
        self.accound_number = random.randint(10000000, 99999999)
        self.history = []
        self.history.append(f"account created with saldo: {start_saldo}")
    def deposit(self, amount):
        if amount < 0 or self.reception == False:
            print("Transaction failed")
        else: 
            self.start_saldo = self.start_saldo + amount 
            self.history.append(f"Deposit: {amount}, new saldo: {self.start_saldo}")
            return self.start_saldo 
    def withdraw(self, amount): 
        if(self.start_saldo - amount) < -self.credit_limit or amount <= 0 or self.reception == False: 
            print("Transaction has failed")
        else: 
            self.start_saldo = self.start_saldo - amount 
            self.history.append("Withdrawn: {amount}, new saldo: {self.start_saldo}")
            return self.start_saldo 
    def transfer(self, receiver, amount): 
        if(self.start_saldo - amount) < -self.credit_limit or amount <= 0 or self.reception == False: 
            print("Transaction has failed")
        else: 
            receiver.start_saldo = receiver.start_saldo + amount 
            self.start_saldo = self.start_saldo - amount 
            self.history.append(f"Transfer: {amount} to {receiver.name}")
            self.history.append(f"Received: {amount}, from {self.name}")
            return receiver.start_saldo, self.start_saldo 
    def show_saldo(self):
        return self.name, self.start_saldo 
    def add_interest_rate(self, percentage):
        increase = self.start_saldo * percentage 
        self.start_saldo += increase 
        self.history.append(f"Interest rate added with {percentage*100}%, new saldo: {self.start_saldo}")
        return self.start_saldo 
    def show_transactions(self):
        print(f"\n Transaction history for {self.name}")
        for trans in self.history: 
            print(trans)
    def __str__(self):
        return f"Customers name: {self.name}, account number: {self.account_number}, saldo: {self.start_saldo}"

class Bank():
    def __init__(self): 
        self.customers = []
    def add_customer(self, customer):
        self.customers.append(customer)
    def total_saldo(self):
        total = 0 
        for customer in self.customers: 
            total += customer.start_saldo 
        return total 
    def find_customer(self, search_word):
        for cust in self.customers: 
            if customer.name.lower() == str(search_word) or str(customer.account_number) == str(search_word):
                return customer 
        return None 

bank = Bank()
Jess = BankCustomer("Jess", 100, True)
Noor = BankCustomer("Noor", 1000, True)
Customers = []
Customers.append(Jess)
Customers.append(Noor)
bank.add_customer(Jess)
bank.add_customer(Noor)

## CLASSES AND SUBCLASSES 
### EX. TASK 1 -- ANIMALS 
class Animal: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def sound(self):
        print(f"Animal: {self.name}, is {self.age} years old")
### EX. TASK 2 -- VEHICLES 
### EX. TASK 3 -- PEOPLE 

## CLASSES AND WHOLE LOTTA BULLSHIT 
### EX. TASK 1 -- ONLY TASK 
