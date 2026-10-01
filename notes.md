# NOTES 

## AI HELP 

### SPARA I JSON 
``` py
        for a in accounts: 
            json_str = json.dumps(a.__dict__, indent=4)
            with open("accs.json", "w") as f: 
                f.write(json_str) 
```
Sparar **en** user för varje session som händer i en json fil. 

#### NEW ATTEMPT WITH CLASS 
``` py
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

out = []

def menu():
    while True:
        print("\nYo wassup cuh!")
        print("Mess around with this program for me wotn ya?")
        print("1. Create a new animal")
        print("2. View all them animals")
        print("3. Search for an animal")
        print("4. Delete an animal")
        print("5. Exit the program")

        choice = input("whatchu wanna do?: ")

        if choice == "1":
            name = input("whas the name? ")
            age = input("how old is it? ")
            desc = input("gimme a short description: ")
            new_animal = Animal(name, age, desc)
            out.append(new_animal)
            
        elif choice == "2":
            if not out: 
                print("there are none, buddy")
            else:
                for animal in out: 
                    print(animal)
                    
        elif choice == "3":
            search = input("Who you searchin? ")
            found = False 
            for a in out: 
                if a.name == search:
                    found = True 
                    print(a)
                    break
            if not found: 
                print("no such animal, pal")
                
        elif choice == "4":
            delete = input("who's getting deleted cuh? ")
            found = False 
            for a in out: 
                if a.name == delete: 
                    found = True
                    out.remove(a)
                    print(f"{delete} has been deleted")
                    break
            if not found:
                print("no such animal to delete, pal")
                
        elif choice == "5":
            print("Peace out!")
            break
        else:
            print("Invalid choice, try again.")

# Run the menu program
menu()

# Convert all Animal objects to dictionaries using to_dic() before saving
animals_data = [animal.to_dic() for animal in out]

with open('animals.json', 'w') as file: 
    json.dump(animals_data, file, indent=4)
    print("Saved animals to animals.json successfully!") 
```


## OTHER HELP -> WEBSITES & PEOPLE 
``` py
# Source - https://stackoverflow.com/a/66551656
# Posted by MrFoot fifer
# Retrieved 2026-10-01, License - CC BY-SA 4.0

import json

def get_studentdetails():
    data={}
    data['name']=input("Enter Student name")
    data['class']=input("Enter Class")
    data['maths']=input("Enter Marks for Maths")
    data['eng']=input("Enter English Marks")
    data['sci']=input("Enter Science Marks")
    return (data)
out=[]
while True:
    quit=input("Enter Y/N to continue")
    if quit.lower() == 'n':
        break
    record = get_studentdetails()
    out.append(record)


with open('students.json','w') as file:
    json.dump(out,file,indent=2)

```
*https://stackoverflow.com/questions/66551592/how-to-store-input-values-from-user-in-json-format*

``` py
# Source - https://stackoverflow.com/a/66551772
# Posted by HadiB
# Retrieved 2026-10-01, License - CC BY-SA 4.0

with open('students.json','w') as file:
    json.dump(out,file,indent=2)

```

