class Rektangel:
    def __init__(self, l, b):
        self.längd = l 
        self.bredd = b
    def area(self):
        return self.längd * self.bredd
    def omkrets(self):
        return 2 * self.längd + 2 * self.bredd 
    def __str__(self):
        return f"Rektangelns längd: {self.längd}, bredd: {self.bredd},"
        
Rektanglar = []
a = Rektangel(5, 10)
b = Rektangel(6, 12)
c = Rektangel(7, 9)
d = Rektangel(4, 24)
Rektanglar.append(a)
Rektanglar.append(b)
Rektanglar.append(c)
Rektanglar.append(d)

for r in Rektanglar: 
    print(r, "area:", r.area(), "omkrets:", r.omkrets())



    