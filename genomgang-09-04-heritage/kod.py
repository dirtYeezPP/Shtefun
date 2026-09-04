class Person:
    def __init__(self, name, birth_year): #
        self.name = name  # vad den heter internt --> variabelnamn inte samma sak!!! 
        self.birth_year = birth_year
        print(f"Person {self.name} skapad, född {self.birth_year}")

    def __str__(self):
        return(f"Personens namn: {self.name}, född: {self.birth_year}") 
        # return(self.name, self.birth_year) --> print(p) --> typeerror string return nonstring tuple 
        # vi kan inte använda komma vid return av komplexa strängar, det funkar i print men inte i return, då tror den att det är en tuple. 
        # det är en av anledningarna att vi använder f-strings, för att vi kan returnera en sträng som är komplex.
    def vacation(self): 
        print(f"{self.name} has gone on vacation!")



class Teacher(Person): # du kan inte skapa en lärare, det är en person och då måste vi ha namn och födelseår! du kan inte skapa läraren utan det. 
    # namn och födelseår finns i Person klassen, vi vill inte skriva här utan vi kan låta de vara där. 
    # säga till att den ska använda den där uppe 
    def __init__(self, name, birth_year, pay):
        super().__init__(name, birth_year) # super klassen är den vi har ärvt av! nu skickar vi dessa två dit för att det skall omhändertas där 
        # vi tar hand om de här grejerna inom person klassen, inte i denna. 
        # då printas samma sak som vi sagt åt att printas inom Person klassen, vi måste ju skicka upp de här grejerna, denna omhändertas där. 
        # vi vill skicka upp så mycket som möjligt! vi vill inte ha så mycket nere LOLLLL 
        # men nu.. en lärare kanske har ett jobb och en inkomst, det har inte alla ju rawr 
        # lön kommer inte skickas in, denna skall stanna kvar här 
        self.pay = pay 

    def __str__(self):
        return f"{super().__str__()} pay: {self.pay}" #den returnerar det som finns där uppe men vi vill ju fylla på även om vi återanvänder 
        # yayyy nu skriver den ut allting!!! om vi kommer på att vi vill skriva ut nå mer om personen
        # typ två mellanslag i namn, gör jag det i person klassen så vid utskriften av (str metoden i person) 
        # när vi ändrar där kommer det automatiskt att ändras i lärarklassen såklart yuhh för den ärver. 

class Student(Person): 
    def __init__(self, name, birth_year, classs):
        super().__init__(name, birth_year)

        self.classs = classs 

    def __str__(self):
        return f"{super().__str__} class: {self.classs}"

    def vacation(self):
        print(f"lol, F in chat, student tried to go on vacation.")

# alla som ärver men vi vill kanske overridea en metod i en klass med något annat, då är det bara att skriva en med samma namn
# skriver vi inget kommer de ju bara att ärvas yaaaa
# då kan han skapa en lista 

p = Person("Stefan", 1973)
Teach1 = Teacher('Freddy', 1979, 20000)
Student1 = Student("Melker", 2007, "HR26")

personlista = []
personlista.append(Teach1)
personlista.append(Student1)
personlista.append(Student('Polina', 2007, 'TE467IT')) #tänk om några år haheuehhehaha stefan jokster 

print(Teach1)
print(Student1)
Student1.vacation()

for person in personlista: 
    print(person)
    person.vacation() # alternativen av funktionerna dyker inte upp, eftersom systemet inte vet att personlistan har bara personer 
    # därför kommer det inte kunna hjälpa oss här, dock går det ju att köra funktionen ändå. 
    # ser vit ut, som om det inte funkar men de bara trick. 

    # med arv kan vi skapa en bas klass 
    # fördel med den strukturen är att vi kan enkelt skapa subklasser och sedan fylla på med information utifrån primärklassen. 
    # super --> hänvisar alltid tillbaka till bas klassen 
    

