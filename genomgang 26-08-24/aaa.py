# klass som en mall yuh 
class Bil: 
    #vars, props, egenskaper, attribut, de tillhör en klass. 
    brand = ""
    model = ""

# skapa instans av en klass eller ett objekt 
b = Bil()
b.brand = "Volvo"
b.model = "XC90"
#print(b)

c = Bil()
c.brand = "Saab"
c.model = "9-5" 
#print(c)

#skapa en lista med bilar 
bilar = []
bilar.append(b)
bilar.append(c)
print(bilar) #här får vi ts weird stuff that we get when printing "b", or well the instance of the class. 
print(bilar[0].brand) #här får vi ut "Volvo" som är brand på första objektet i listan.


