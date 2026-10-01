import json 



def menu():
    print("" \
    "Hi i want to test this stuff" \
    "Please follow the instructions given so i can proceed.")

def get_data(): 
    name = input("give me a name: ")
    age = input("give me an age: ")
    desc = input("give me a SHORT description: ")

    data = {
        "name": name,
        "age": age,
        "description": desc
        }
    return data
 
out = []

while True:
    q = input("enter Y/N to continue or exit: ")
    if q.lower() == "n":
        break 
    rec = get_data()
    out.append(rec)

with open('./testsav.json', 'w') as file: 
    json.dump(out, file, indent=4)




    