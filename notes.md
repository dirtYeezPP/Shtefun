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
# Convert all Animal objects to dictionaries using to_dic() before saving
animals_data = [animal.to_dic() for animal in out]
```
It was also suggested to call the to_dic() function upon animal creation. 

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

