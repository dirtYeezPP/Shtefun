class Vehicle: 
    def __init__(self, model, brand, year):
        self.model = model 
        self.brand = brand
        self.year = year 

    def __str__(self):
        return(f"model: {self.model}, brand: {self.brand}, made year: {self.year}")

    def description(self): 
        return f"Vehicle is a: {self.model} cool cool it goes broom broom"
    def is_veteran(self):
        return (self.year - 2026 == 30)

class Car(Vehicle):
    def __init__(self, model, brand, year):
        super().__init__(model, brand, year)
    def __str__(self):
        return f"Car is a {super().__str__()}"

class Motorbike(Vehicle):
    def __init__(self, model, brand, year):
        super().__init__(model, brand, year)
    def __str__(self):
        return f"Motorbike is a {super().__str__()}"

