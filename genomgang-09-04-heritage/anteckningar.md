# GENOMGÅNG 09/04 --> KLASSER OCH ARV 

klass av någon typ --> fler klasser som liknar den exempelvis monster klass men vi vill skapa många olika typer av monster. 
Säg vi ska skapa två med liknande egenskaper men de skiljer sig åt. Goblin och en Orc. Vissa saker har de gemensamt, typ alla har hp
själva hp attributet är i monster, ad också, men så kan det finnas vissa grejer som skiljer monsterna åt. 
Race i monster. 
Model i monster. 
speed i monster.
BODY COUNT???? NOOR ON CRAAZY SHIII


## LETS GET SERIOUS 
FORDON --> tillverkare, däck, årsmodell.... färg 
Bilar --> antal dörrar
Motorcyklar --> sidovagn? 

de kommer automatiskt få de här attributen uppe i fordon. 
subklass --> en bil är ett fordon! 

``` py 

``` 

``` py 

```






``` py 
```

``` py 
```

``` py 
```

``` py 
```

``` py 
```

``` py 
```

``` py 
```

``` py 

class Person:
    def __init__(self, name, pers_identity_num):
        self.name = name 
        self.pers_identity_num = pers_identity_num

    def description(self):
        return f"Person: {self.name}, personal identity number: {self.pers_identity_num}"

    def greet(self): 
        return "rawr"

    def __str__(self):
        return f"Person with name: {self.name}, and identity number: {self.pers_identity_num}"


class Employed(Person): 
    def __init__(self, name, pers_identity_num, greeting):
        super().__init__(name, pers_identity_num)
        self.greeting = greeting

    def description(self):
        return f"Employed person: {self.name}"

    def greet(self):
        return f"{self.name} says {self.greeting}"


class Teacher(Employed): 
    def __init__(self, name, pers_identity_num, subject, greeting):
        super().__init__(name, pers_identity_num, greeting)
        self.subject = subject 

    def description(self):
        return f"{super().description()}, teaches: {self.subject}" 


class Principal(Employed):
    def __init__(self, name, pers_identity_num, responsibility_area, greeting):
        super().__init__(name, pers_identity_num, greeting)
        self.responsibility_area = responsibility_area

    def description(self):
        return f"{super().description()}, is responsible in: {self.responsibility_area}"


# --- Menyfunktioner ---

peeps = [
    Teacher("Robert O", "081729733737", "Cisco", "Goodday"),
    Principal("Maria B", "9384834738", "Technology department", "HIIII")
]

def skapa_person():
    print("\nVad för typ av person vill du skapa?")
    print("1. Vanlig person\n2. Lärare (Teacher)\n3. Rektor (Principal)")
    roll = input("Välj (1-3): ").strip()
    
    name = input("Namn: ").strip()
    pers_num = input("Personnummer: ").strip()
    
    if roll == "1":
        peeps.append(Person(name, pers_num))
    elif roll == "2":
        subject = input("Ämne: ").strip()
        greeting = input("Hälsning: ").strip()
        peeps.append(Teacher(name, pers_num, subject, greeting))
    elif roll == "3":
        area = input("Ansvarsområde: ").strip()
        greeting = input("Hälsning: ").strip()
        peeps.append(Principal(name, pers_num, area, greeting))
    else:
        print("Ogiltigt val.")
        return
    print(f"{name} har lagts till!")

def lista_alla_personer():
    if not peeps:
        print("\nInga personer registrerade.")
        return
    print("\n--- Alla personer ---")
    for i, p in enumerate(peeps, 1): # start at one, i is the number counter --> p the individual object for turn of the loop
        print(f"{i}. {p.name} ({p.__class__.__name__}) - {p.pers_identity_num}")
        #fetches name of class that created the object as a string 
        # if p is a teacher instance, p.__class__ --> refers to <class 'main__.Teaceher__'>
        # __name__ pulls just "Teacher"

def hitta_person(pers_num):
    for p in peeps:
        if p.pers_identity_num == pers_num:
            return p
    return None

def visa_person():
    pers_num = input("\nAnge personnummer på personen du vill visa: ").strip() #take away spaces beg and end
    person = hitta_person(pers_num)
    if person:
        print(f"\nInfo: {person}")
        print(f"Beskrivning: {person.description()}")
        print(f"Hälsning: {person.greet()}")
    else:
        print("Kunde inte hitta personen.")

def andra_personinfo():
    pers_num = input("\nAnge personnummer på personen som ska ändras: ").strip()
    person = hitta_person(pers_num)
    if not person:
        print("Kunde inte hitta personen.")
        return
    
    nytt_namn = input(f"Nytt namn (lämna tomt för att behålla '{person.name}'): ").strip()
    if nytt_namn:
        person.name = nytt_namn
        
    if isinstance(person, Employed):
        ny_halsning = input(f"Ny hälsning (lämna tomt för '{person.greeting}'): ").strip()
        if ny_halsning:
            person.greeting = ny_halsning
            
    if isinstance(person, Teacher):
        nytt_amne = input(f"Nytt ämne (lämna tomt för '{person.subject}'): ").strip()
        if nytt_amne:
            person.subject = nytt_amne
            
    elif isinstance(person, Principal):
        nytt_omrade = input(f"Nytt ansvarsområde (lämna tomt för '{person.responsibility_area}'): ").strip()
        if nytt_omrade:
            person.responsibility_area = nytt_omrade

    print("Personinformationen uppdaterades!")

def ta_bort_person():
    pers_num = input("\nAnge personnummer på personen som ska tas bort: ").strip()
    person = hitta_person(pers_num)
    if person:
        peeps.remove(person)
        print(f"{person.name} togs bort.")
    else:
        print("Kunde inte hitta personen.")


# --- Huvudloop ---

def main():
    while True:
        print("\n--- MENY ---")
        print("1. Skapa person")
        print("2. Lista alla personer")
        print("3. Visa person")
        print("4. Ändra personinfo")
        print("5. Ta bort person")
        print("6. Avsluta")

        val = input("Välj ett alternativ (1-6): ").strip()

        if val == "1":
            skapa_person()
        elif val == "2":
            lista_alla_personer()
        elif val == "3":
            visa_person()
        elif val == "4":
            andra_personinfo()
        elif val == "5":
            ta_bort_person()
        elif val == "6":
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val, försök igen.")

main()
```