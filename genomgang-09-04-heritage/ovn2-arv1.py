class Vehicle: 
    def __init__(self, model, brand, year):
        self.model = model 
        self.brand = brand
        self.year = year 

    def __str__(self):
        return(f"model: {self.model}, brand: {self.brand}, made year: {self.year}")

    def description(self): 
        return f"Vehicle is a: {self.model}, brand: {self.brand} and made year: {self.year}"
    def is_veteran(self):
        return (2026 - self.year >= 30)

class Car(Vehicle):
    def __init__(self, model, brand, year, doors_amount):
        super().__init__(model, brand, year)
        self.doors_amount = doors_amount 
    def description(self):
        return f"{super().description()}, which has {self.doors_amount} doors"
    
    def __str__(self):
        return f"Car is a {super().__str__()}, it has {self.doors_amount} doors"

class Motorbike(Vehicle):
    def __init__(self, model, brand, year, has_sidecar):
        super().__init__(model, brand, year)
        self.has_sidecar = has_sidecar
    def __str__(self):
        return f"Motorbike is a {super().__str__()}, has sidecar: {self.has_sidecar}"

m1 = Motorbike("R6 RACE", "Yamaha", 2000, False)
car1 = Car("V70", "Volvo", 1976, 4)
m2 = Motorbike("YZ450F", "Yamaha", 2026, False)

vehicles = []
vehicles.append(m1)
vehicles.append(m2)
vehicles.append(car1)
#print(m1.is_veteran())

for vehicle in vehicles: 
    print(vehicle)
    print(vehicle.is_veteran())

