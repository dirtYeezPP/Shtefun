class Pokemon: 
    poke_amount = 0 # klassvariabel som tllhör klassen och inte en pokemon (ingen instans)
    # alla pokemon har eget namn och allt men de har inte antalet pokemon
    # print(pokemon.poke_amount) yuh 
    # nu är den hemlig yes om vi inte vill att nå ska kunna ändra det utifrån sen. 
    #men vi vill öka den varje gång en poke läggs till 
    def __init__(self, name, HP):
        self.hp = HP 
        #self._name = name 
        #En variabel med underscore är en privat sådan 
        #är tänkt att inte ändras utanför denna klass 
        # self.__name = name istället och testar sen och det funkade då inte att ändra den utanför wooeoowo 
        # genom 2 så ser det ut som att vi inte kan ändra den överhuvudtaget, dvs den privata ändras inte. 
        #men hur ska vi få fram den? 
        self.__name = name  # existerar här ine men åtkomst finns ej utanför 
        #men vi kanske vill komma åt den ändå ykwim? properties 
        self.type = ""
        Pokemon.poke_amount += 1 #yurhh letsgoooo
    def __str__(self):
        return f"pokemon named {self.__name} \n HP: \t {self.hp}" #t är tab yes 
    
    #properties 
    @property # en getter! 
    #genom att göra detta de en funktion men den gör att vi kan skriva wp1._name och komma åt namnet med propertyn! 
    def name(self): #name är variabelnamnet yes 
        # de en funktion som inte anrpas med paranteser, det kommer utifrån att se ut som att de bara en vanlig variabel från klassen "self.name = name". 
        return self.__name 
    #ändra namnet utifrån men vi vill ha en kontroll! typ vissa regler! i.e. mejl kontrllerar att de actual mejl 
    @name.setter #setter
    def name(self, new_name):
        # ändra namn på pokemo men vi vill ha en kontroll
        if len(new_name)>0:
            self.__name = new_name 
        else: 
            print(f"youre a nub bro")
    # skydda / kapsla in information 
    #varje gng med self --> tillhör viss instans av ett objekt, liksom just den grejen vi vill komma åt 
    # men om metoden tillhör klassen? den ska inte tillhöra varje instans utan själva klassen. i.e. räknare 
    # klass metod --> tillhör klassen och inte en instans av ett objekt, inte en specifik pokemon dvs 
    @classmethod 
    def num_of_pokes(cls): #ingen self för den hänvisar till en specifik instans 
        return cls.poke_amount 
    # behöver använda cls och cls.etc, en variabel som tillhör klassen och inte något av objekten. printa detta sen yus 

    #statiska metoder 
    @staticmethod #static --> 
    # public --> alla, private --> privat spklart 
    # void --> returnerar inget, static --> statisk! den ändras inte meeeennnn skillnad? 
    # klassmetoder existerar inte direkt överallt 
    # statisk metod tillhör en klass och / men vi behölver inte ens skapa en instans för att 
    # använda dessa 
    #de är helt kopplade till klassen, inte till nå instans. 
    def addition(t1,t2):
        return t1+t2 
    # köra en statisk metod 
    # print(pokemon.addition(1,6))
    # vi kan skapa en klass med funktioner där vi inte behöver skapa nå först föär att anävnda de 
    # i.e. en massa metoder med matematik, vi behlver inte matte objekt eller så 
    # i.e. databaskopplingar allt sådant, dv klass 
    # static method används ofta med variabler, de är inte kopplade till en instans de kan användas utan att skapa instanser 
    # public static void main
    # kan jag köra den utan att skapa en instans av klassen som den ligger i. 

class waterPoke(Pokemon): 
    def __init__(self, name, HP):
        super().__init__(name, HP)
        self.type = "Water"
    def __str__(self):
        return f"{super().__str__()} \n Type: {self.type} "

wp1 = waterPoke("Squirtle", 67)
print(wp1)
#wp1.name = "" #det gick inte att ändra namnet 
wp1.name = "Steffe"
print(wp1) # ts works, it looks like it has a variable but weve made a whole control thingy for it! 
# alla vars vi skapar ska vara satta till private om inte vi kan ge bra anledning till varför vi inte har gjort det! 
# bara getter --> i.e. bara hämta namnet, ibland kanske det inte behövs att ändra något! i.e. personnummer. 

#wp1._name = "Arne" # dont do this bro please 

#print(wp1._name)
# det går inte! den påstår att det inte finns nå sånt attribut men vi vet ju att vi har det
# med två --> vi kan men kan  inte komma åt den (stökig kod) 



# kan göra det yurh men det kanske vi inte vill att man ska kunna göra 
"""
ex instanser elle rklasser eller så
self._name men nu går det 
så när vi sätter den där i name så gör vi den en private variabel
den tillhör klassen pokemon LOL han måste ju ändra det överallt  
alltid när vi ser underscore 
"""


# __ --> dölja 
# _ --> visa att vi inte skall pila på den men vi kan 
# getters och setters --> olika i olika språk med samma princip
# prvata variabler som v iskyddar men kommer åt de utanför med getter
#setter kunna ändra den med någon typ av kontroll most of the time. 
# klass metoder 
#specifikt i pyton lite men har vi en klass var och vill göra nå med den kan vi komma åt den genom cls 
#funkar inte med self, de tillhör klassen#
#static --> behöver inte skapa nå instanser, den kan köras js like that, 
# lägga metoder för sig för att sedan komma åt de senare 

# variabler same
# i.e. lägg i klass moch sen hämta med hjälp av det, class.gay liksom pokemon.addera 
# de tillhör klassen inte instansen, instans --> objekt namnet. --> wp1.name exempelvis 
