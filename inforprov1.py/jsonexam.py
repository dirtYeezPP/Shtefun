import json 

class Account:
    __acc_amount = 0
    def __init__(self, username, password, role):
        self.__username = username
        self.__password = password 
        self.__active = True 
        self.role = role 
        Account.__acc_amount += 1 

    @property 
    def password(self): 
        return self.__password
    @property 
    def active(self): 
        return self.__active 
    @property 
    def role(self): 
        return self.__role 
    @property 
    def username(self): 
        return self.__username 

    @role.setter 
    def role(self, newr): 
        permitted = ["admin", "member", "guest"]
        if newr in permitted: 
            self.__role = newr 
        else: 
            print(f"{newr} is gay, youre a guest now")
            self.__role = "guest"

    def is_active(self): 
        return self.__active 
    def inactivate(self): 
        self.__active = False 
        print(f"acc now inactivated")
    def activate(self): 
        self.__active = True 
        print(f"acc activated")

    def authenticate(self, name, password): 
        return name == self.__username and password == self.__password 

    def change_password(self, pswrd): 
        if(len(pswrd) >= 6): 
            self.__password = pswrd 
            print("password updated")
        else: 
            print("you little dipshit") 

    def get_dic(self): 
        dic = {
            "username": self.__username, 
            "password": self.__password,
            "role": self.__role, 
            "active": self.__active 
        } 
        return dic 

    def __str__(self):
        status = "Active" if self.__active else "inactive"
        return f"Acc: {self.__username}, Role: {self.__role}, Status: {status}"

    @classmethod 
    def show_acc_amount(cls): 
        return cls.__acc_amount

def menu(): 
    accounts = []

    while True: 
        print("\n Hello there fellow fellow fellow" \
        "\n 1. Create account" \
        "\n 2. Show all acccounts" \
        "\n 3. Change password" \
        "\n 4. Inactivate your account" \
        "\n 5. Activate account" \
        "\n 6. Authenticate user " \
        "\n 7. Show the amount of accounts that exist" \
        "\n 8. exit program")

        choice = input("what do you wish to do?: ")

        if choice == "1": 
            name = input("a name please: ")
            pswrd = input("a password please: ")
            role = input("role? permitted are guest, member, admin: ")
            new = Account(name, pswrd, role) 
            accounts.append(new)

        elif choice == "2":
            if not accounts: 
                print("no accs")
            for acc in accounts: 
                print(acc)
        elif choice == "3": 
            nem = input("gib user: ")
            found = False 
            for a in accounts: 
                if a.username == nem: 
                    found = True 
                    pswrd = input("new pass: ")
                    a.change_password(pswrd)
                    break 
                if not found: 
                    print("no such acc bozo")
        elif choice == "4":
            user = input("which user?: ")
            found = False 
            for a in accounts: 
                if a.username == user: 
                    found = True 
                    a.inactivate()
                    break 
                if not found: 
                    print("No user")
        elif choice == "5": 
            name = input("write the username: ")
            found = False 
            for a in accounts: 
                if a.username == name: 
                    found = True 
                    a.activate()
                    break 
                if not found: 
                    print("no such user")
        elif choice == "6": 
            name = input("name: ")
            pswrd = input("pass: ")
            found = False 
            for a in accounts: 
                if a.username == name: 
                    found = True 
                    if a.authenticate(name, pswrd): 
                        print("auth successful")
                    else: 
                        print("nub")
                    break 
                if not found: 
                    print("no acc like that")
        elif choice == "7": 
            am = Account.show_acc_amount()
            print(f"accs: {am}")
        elif choice == "8":
            print("ending program")
            break 
        else: 
            print("there is no such option, try again")



if __name__ == "__main__":
    menu()
