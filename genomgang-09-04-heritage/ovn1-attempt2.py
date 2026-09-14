class Animal: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def __str__(self):
        return(f"The animals name: {self.name}, and age: {self.age}")
    def sound(self): 
        return(f"roooaaaaarrrrr")
    def description(self):
        return(f"name: {self.name}, age: {self.age}")
    def feed(self):
        return(f"bro eating")
    def play(self):
        pass 

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

        #yo nevermind 