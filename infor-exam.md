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


``` py
class Katt:
    def __init__(self, namn):
        # Ett understreck (_) betyder "Detta är en privat variabel, rör den inte direkt!"
        self._namn = namn 

    # 1. GETTER: Så här gör vi för att hämta (läsa) namnet
    @property
    def namn(self):
        return self._namn

    # 2. SETTER: Så här gör vi för att ändra namnet (med en säkerhetskoll!)
    @namn.setter
    def namn(self, nytt_namn):
        if len(nytt_namn) >= 2:
            self._namn = nytt_namn
        else:
            print("Fel: Namnet måste vara minst 2 bokstäver långt!")

# Användning:
min_katt = Katt("Missan")
print(min_katt.namn)      # Anropar gettern (skriver ut "Missan")
min_katt.namn = "Bo"      # Anropar settern (godkänns!)
min_katt.namn = "X"       # Anropar settern (vakten stoppar detta och skriver ut felmeddelandet)

```


``` py
class Anvandarkonto:
    # Klassvariabel (delas av alla konton). 
    # Två understreck (__) gör den strikt privat.
    __antal_konton = 0 

    def __init__(self, anvandarnamn, losenord, roll):
        self._anvandarnamn = anvandarnamn
        self._losenord = losenord
        self._aktiv = True
        
        # När vi sätter rollen här, kommer den automatiskt gå via settern nedan!
        self.roll = roll 
        
        # Öka räknaren varje gång ett nytt konto skapas
        Anvandarkonto.__antal_konton += 1

    # --- PROPERTIES (Vakterna) ---

    @property
    def roll(self):
        return self._roll

    @roll.setter
    def roll(self, ny_roll):
        # Validering: Rollen MÅSTE vara en av dessa tre
        giltiga_roller = ["admin", "medlem", "gäst"]
        if ny_roll in giltiga_roller:
            self._roll = ny_roll
        else:
            print(f"Fel: '{ny_roll}' är ogiltig. Sätter rollen till 'gäst'.")
            self._roll = "gäst"

    # --- VANLIGA METODER ---

    def byt_losenord(self, nytt_losenord):
        if len(nytt_losenord) >= 6:
            self._losenord = nytt_losenord
            print("Lösenordet har uppdaterats!")
        else:
            print("Fel: Lösenordet måste vara minst 6 tecken.")

    def inaktivera(self):
        self._aktiv = False

    def aktivera(self):
        self._aktiv = True

    def ar_aktiv(self):
        return self._aktiv

    def autentisera(self, in_namn, in_losenord):
        # Returnerar True om både namn och lösenord matchar
        return self._anvandarnamn == in_namn and self._losenord == in_losenord

    def __str__(self):
        # Bestämmer hur kontot ser ut om vi printar det
        status = "Aktivt" if self._aktiv else "Inaktivt"
        return f"Konto: {self._anvandarnamn} | Roll: {self._roll} | Status: {status}"

    # --- KLASSMETOD ---
    @classmethod
    def visa_antal_konton(cls):
        return cls.__antal_konton
```

``` py
def huvudmeny():
    # En lista som sparar alla skapade konton
    alla_konton = []

    while True:
        print("\n--- KONTOHANTERAREN ---")
        print("1. Skapa nytt konto")
        print("2. Visa alla konton")
        print("3. Visa antal skapade konton")
        print("4. Avsluta")
        
        val = input("Välj ett alternativ (1-4): ")

        if val == "1":
            namn = input("Ange användarnamn: ")
            losen = input("Ange lösenord: ")
            roll = input("Ange roll (admin/medlem/gäst): ")
            
            # Skapa objektet och lägg till det i listan
            nytt_konto = Anvandarkonto(namn, losen, roll)
            alla_konton.append(nytt_konto)
            print("Kontot har skapats!")

        elif val == "2":
            print("\n-- Alla konton --")
            for konto in alla_konton:
                print(konto) # Detta anropar automatiskt __str__ metoden

        elif val == "3":
            antal = Anvandarkonto.visa_antal_konton()
            print(f"\nTotalt antal skapade konton: {antal}")

        elif val == "4":
            print("Avslutar programmet...")
            break # Bryter loopen

        else:
            print("Ogiltigt val, försök igen.")

# Starta programmet
if __name__ == "__main__":
    huvudmeny() 
```



Programmeringsuppgift: Skapa ett användarkontosystem 

Syfte 

Du ska skapa ett program som hanterar användarkonton i ett digitalt system. Uppgiften tränar på objektorienterad programmering, inklusive konstruktorer, instansvariabler, klassvariabler, metoder, egenskaper och menybaserad interaktion. 

Del 1 – Skapa klassen Användarkonto 

Du ska skapa en klass som representerar ett användarkonto med följande egenskaper: 

Instansvariabler OBS! Alla instansvariabler skall vara ”private” och ha en @property. Gör en @property.setter där du tycker att det är lämpligt    

    användarnamn – sträng 

    lösenord – sträng 

    roll – sträng (t.ex. "admin", "medlem", "gäst") 

    aktiv – bool (True/False) 

Klassvariabel OBS! ska vara ”private” 

    antal_konton – håller koll på hur många konton som har skapats 

Metoder och egenskaper 

    __init__() – konstruktor som skapar ett konto 

    __str__() – returnerar en sträng med kontoinformation 

    byt_lösenord(nytt_lösenord) – ändrar lösenordet om det är minst 6 tecken 

    inaktivera() – sätter kontot till inaktivt 

    aktivera() – sätter kontot till aktivt 

    är_aktiv() – returnerar True/False 

    autentisera(användarnamn, lösenord) – returnerar True om uppgifterna stämmer 

    roll – egenskap med validering (måste vara "admin", "medlem" eller "gäst") 

    antal_konton() – klassmetod som returnerar antalet skapade konton 

 

  

Del 2 – Menybaserad interaktion 

Skapa ett program som använder en meny i terminalen för att hantera konton. Menyn ska innehålla följande alternativ: 

    Skapa nytt konto 

    Visa alla konton 

    Byt lösenord 

    Inaktivera konto 

    Aktivera konto 

    Autentisera användare 

    Visa antal konton 

    Avsluta programmet 

Programmet ska fortsätta visa menyn tills användaren väljer att avsluta. 

 

Del 3 – Testa ditt system 

Testa ditt program genom att: 

    Skapa minst tre konton med olika roller 

    Byta lösenord på ett konto 

    Inaktivera och aktivera ett konto 

    Autentisera en användare med rätt och fel uppgifter 

    Visa det totala antalet konton 

 

Extra: Lägg till funktionalitet för att spara och läsa konton till/från en fil. 