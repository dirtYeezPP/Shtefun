class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def __str__(self):
        return(f"Animal named: {self.name}, is {self.age} years old.")
    def sound(self): 
        print(f"raaaaaawr")
    def description(self): 
        print(f"Animal with name: {self.name}, and age: {self.age}")
    def feed(self): 
        print(f"The animal is eating")
    def play(self): 
        print(f"animal is playing")

class Dog(Animal): 
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"{super().__str__()}"

    def sound(self): 
        print("woof!")
    def feed(self): 
        print("the dog is eating happily")
    def play(self):
        print(f"dog is playing with bone toy")

class Cat(Animal): 
    def __init__(self, name, age):
        super().__init__(name, age)
    def __str__(self):
        return f"{super().__str__()}"
    def sound(self): 
        print("meow")
    def feed(self):
        print("the cat is being picky")
    def play(self): 
        print(f"cat is not very interested in that mouse toy")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"{super().__str__()}"

    def sound(self):
        print("KVITTER")
    def feed(self): 
        print("its nibbling on some seeds")
    def play(self):
        print(f"the bird is flying round n round")

animalList = []

animalList.append(Dog("bosse", 5))
animalList.append(Cat("lucinator", 3))
animalList.append(Bird("bub", 3))

for animal in animalList:
    print(animal)
    animal.sound()
    animal.description()
    animal.feed()
    animal.play()


