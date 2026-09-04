class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def sound(self): 
        print(f"raaaaaawr")
    def description(self): 
        print(f"Animal with name: {self.name}, and age: {self.age}")
    def feed(self): 
        print(f"The animal is eating")

class Dog(Animal): 
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self): 
        print("woof!")
    def feed(self): 
        print("the dog is eating happily")

class Cat(Animal): 
    def __init__(self, name, age):
        super().__init__(name, age)
    def sound(self): 
        print("meow")
    def feed(self):
        print("the cat is being picky")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self):
        print("KVITTER")
    def feed(self): 
        print("its nibbling on some seeds")
