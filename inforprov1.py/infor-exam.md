# NOTES 

## AI HELP 
``` py
        for a in accounts: 
            json_str = json.dumps(a.__dict__, indent=4)
            with open("accs.json", "w") as f: 
                f.write(json_str) 
```
Sparar en user för varje session som händer i en json fil. 


