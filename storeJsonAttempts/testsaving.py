import json 

def get_data(): 
    data = {}
    data['name'] = input("give me a name: ")
    data['age'] = input("give me an age: ")
    data['desc'] = input("give me a SHORT description: ")
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




    