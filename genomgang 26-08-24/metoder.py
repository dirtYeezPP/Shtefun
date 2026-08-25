#Metod - funktion som tillhör en klass. 
class car: 
    breed = ""
    loaf = ""
    #så länge vi är inne här kan vi lägga in en metod, något katten kan göra. 
    def purr(self): #vi måste ha self som första argument, det är en referens till objektet som anropar metoden. 
        print("purr purr")

c = car()
c.breed = "siamese car"
c.loaf = "7/10"
c.purr() #self räknas inte med som ett attribut som måste skickas med när funktionen körs. 
c2 = car()
c2.breed = "persian car"
c2.loaf = "8/10"
c2.purr() 


#self - hänvisar tillbaka till det aktuella objektet som anropar metoden. 
class dog:
    wag = 0
    woof = 0

    def tail(self):
        return self.wag * self.woof 

d1 = dog()
d1.wag = 5
d1.woof = 3
print(d1.tail()) #här anropar vi metoden tail() på objektet d1 
d2 = dog()
d2.wag = 2
d2.woof = 4
print(d2.tail()) #här anropar vi metoden tail() på objektet d2 



# __init__ - en speciell metod som körs när ett objekt skapas.
# konstruktor/metod/funktion som körs när objektet/instansen för ett objekt skapas.
class Cat: 
    def __init__(self, bred :str, loaf): #self är alltid första argumentet i en metod, behövs i varje funktion i en klass. 
        #Om du inte vill ha nå här så kan du skriva pass, det är en tom funktion som inte gör någonting. 
        #self skickar vi inte med, men de andra attributen skickas med när vi skapar en cat. 
        self.breed = bred #det efter likamedstecknet bör matcha med det som skickas med när vi skapar en cat. 
        self.loaf = loaf 
        print(f"En {self.breed} har skapats!") #f säger att vi vill formatera strängen, och vi kan använda variabler i strängen. används mest i return  

c = Cat("siamese cat", 7)
#Är den tom kommer vi inte kunna köra detta, i med att vi måste skicka in båda argumenten/egenskaperna! 
d = Cat("persian cat", 8)


# __str__ - en speciell metod som körs när vi vill skriva ut ett objekt, 
# bestämmer vad som skrivs ut när vi skriver print(objekt). 
class Mage: 
    def __init__(self, mp, hp):
        self.MP = mp
        self.HP = hp
    def __str__(self):
        return f"MP: {self.MP}, HP: {self.HP}" #detta är det som skrivs ut när vi skriver print(objekt)

#mage list 
mages = []

m = Mage(100, 50)
n = Mage(200, 100)

mages.append(Mage(200, 40))
mages.append(m)
mages.append(n)
print(mages) 

for mage in mages:
    print(mage) #här anropar vi __str__ metoden på varje objekt i listan mages.

