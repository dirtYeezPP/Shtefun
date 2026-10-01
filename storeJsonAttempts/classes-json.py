import json 

class Animal:
    def __init__(self, name, age, desc):
        self.name = name
        self.age = age
        self.desc = desc

    def to_dic(self):
        return {
            "name": self.name,
            "age": self.age,
            "description": self.desc
        }
    
    def __str__(self):
        return f"Animal(name={self.name}, age={self.age}, description={self.desc})"

out=[]

def menu():
    while True: 
        print("Yo wassup cuh!" \
        "\n Mess around with this program for me wotn ya?" \
        "\n 1. Create a new animal" \
        "\n 2. View all them animals" \
        "\n 3. Search for an animal" \
        "\n 4. Delete an animal " \
        "\n 5. Exit the program")

        choice = input("whatchu wanna do?: ")

        if choice == "1": 
            name = input("gimme a name: ")
            age = input("gimme an age: ")
            desc = input("gimme a short description: ")
            new_animal = Animal(name, age, desc)
            # out.append(new_animal.to_dic()) 
            out.append(new_animal)
        elif choice == "2": 
            if not out:
                print("no animals to show")
            for animal in out: 
                print(animal)
        elif choice == "3": 
            search = input("who you searchin? ")
            found = False 
            for a in out: 
                if a.name == search:
                    found = True 
                    print(a)
                    break
            if not found:
                print("no such animal")
        elif choice == "4":
            delete = input("who getting deleted? ")
            found = False 
            for a in out:
                if a.name == delete:
                    found = True 
                    out.remove(a) 
                    print(f"{delete} has been deleted")
                    break 
                if not found: 
                    print("no such animal")
        elif choice == "5":
            print("exiting program")
            break
        else: 
            print("invalid choice, try again")


menu()

# convert all to dictionaries for JSON serialization before saving 
animals = [animal.to_dic() for animal in out]

with open('animals.json', 'w') as file: 
    json.dump(animals, file, indent=4)
    print("Saved animals to animals.json successfully!") 
                
                            