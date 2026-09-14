class Person():
    def __init__(self, name, pers_identity_num):
        self.name = name 
        self.pers_identity_num = pers_identity_num

    def description(self):
        return f"Person: {self.name}, personal identity number: {self.pers_identity_num}"
    def greet(self): 
        return f"rawr"
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

class Teacher(Employed): #multilevel inheritance 
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

peeps = [
    Teacher("Robert O", "0873749", "Cisco", "Goodday"),
    Principal("Maria B", "98478374", "Technology department", "HIIII")
]

def create_peep():
    print("Whos getting created?")
    print("1. Person \n 2. Teacher \n 3. Principal")
    role = input("pick 1 - 3: ")
    name = input("Their name: ")
    pers_num = input("Their personal identity number: ")

    if role == "1":
        peeps.append(Person(name, pers_num)) 
    elif role == "2":
        subject = input("Which subject are they teaching? ")
        greeting = input("what is their greeting word? ")
        peeps.append(Teacher(name, pers_num, subject, greeting))
    elif role == "3":
        area = input("Which area are they responsible in? ")
        greeting = input("Which is their greeting word? ")
        peeps.append(Principal(name, pers_num, area, greeting))
    else: 
        print("Girl that aint a choice")
        return 
    print(f"{name} has been added")

def remove_peep():
    pers_num = input("What is the personal identity number of the person you wish to delete? ")
    person = find_spec_peep(pers_num)
    if person: 
        peeps.remove(person)
        print(f"{person.name} has been deleted")
    else: 
        print(f"Uhm do they even exist brah")

def list_all_peeps():
    if not peeps: 
        print("there are no peeps here brahh")
        return 
    print("EVERYONEEEE")
    for i, p in enumerate(peeps, 1): 
        print(f"{i}. {p.name} ({p.__class__.__name__}) - {p.pers_identity_num}")

def find_spec_peep(pers_num):
    for p in peeps: 
        if p.pers_identity_num == pers_num:
            return p 
        return None     

def change_peep_info():
    pers_num = input("What is the personal identity number of the person? ")
    person = find_spec_peep(pers_num)
    if not person: 
        print("do they exist wallahi")
        return 
    new_name = input(f"New name? Otherwise leave blank - {person.name} ")
    if new_name: 
        person.name = new_name 
    if isinstance(person, Employed):
        new_greeting = input(f"New greeting? Current {person.name} says {person.greeting} ")
        if new_greeting: 
            person.greeting = new_greeting

    if isinstance(person, Teacher):
        new_subject = input(f"New subject? current one for {person.name} is {person.subject} ")
        if new_subject: 
            person.subject = new_subject 
    elif isinstance(person, Principal):
        new_area = input(f"Changed responsibility area? current one for {person.name} is {person.responsibility_area} ")
        if new_area: 
            person.responsibility_area = new_area
    print(f"personal info updated")

def main():
    while True: 
        print("Menu")
        print("1. create person \n 2. list all people \n 3. show specific person \n 4. Change personal info \n 5. delete a person \n 6. nvm")

        choice = input("Choose 1 - 6 " )

        if choice == "1": 
            create_peep()
        elif choice == "2":
            list_all_peeps()
        elif choice == "3":
            find_spec_peep()
        elif choice == "4":
            change_peep_info()
        elif choice == "5":
            remove_peep()
        elif choice == "6":
            print("oka")
            break 
        else: 
            print("that aint a valid choice bruh")


main()