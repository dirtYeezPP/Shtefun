class Account: 
    __acc_amount = 0 
    def __init__(self, username, password, role): 
        self.__username = username 
        self.__password = password 
        self.__role = role 
        self.__active = True  
        Account.__acc_amount += 1 

    @property 
    def role(self): 
        return self.__role 
    @role.setter 
    def role(self, new_role):
        allowed_roles = ["admin", "member", "guest"]
        if new_role in allowed_roles: 
            self.__role = new_role 
        else: 
            print(f"you little fucker, not a {new_role} im setting you to a guest")
            self.__role = "guest" 

    @property
    def username(self): 
        return self.__username 
    @username.setter
    def username(self, new_name): 
        password = input("write your password first bro")
        if(password == self.__password): 
            self.__username = new_name 
        else: 
            print("shes so bad tuntuntuntun tututututuuutnutn")
            return 

    @property 
    def activity(self): 
        return self.__active 

    @property 
    def password(self): 
        return self.__password 

    def activate(self): 
        self.__active = True
    def inactivate(self): 
        self.__active = False 
    def is_active(self): 
        return self.__active 
    
    def change_password(self, new_pass): 
        if len(new_pass) >= 6: 
            self.__password = new_pass
            print("password updated")
        else: 
            print("wrong you fucker")

    def auth(self, in_username, in_password): 
        return in_username == self.__username and in_password == self.__password

    def __str__(self): 
        return f"Acc: {self.__username}, password: hidden wallah, role: {self.__role}"

    @classmethod 
    def show_acc_amount(cls): 
        return cls.__acc_amount