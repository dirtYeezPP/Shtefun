class Bankkund():
    def __init__(self, namn, start_saldo, täckning):
        self.namn = namn
        self.start_saldo = start_saldo 
        self.täckning = täckning 
    
    def insättning(self, belopp):
        if belopp < 0 or self.täckning == False: 
            print("Transaktionen misslyckades")
        else:
            self.start_saldo = self.start_saldo + belopp  
            return self.start_saldo 
    def uttag(self, belopp):
        if self.start_saldo < belopp or belopp < 0 or self.täckning == False: 
            print("Transaktionen misslyckades")
        else: 
            self.start_saldo = self.start_saldo - belopp 
            return self.start_saldo 
    def överföring(self, mottagare, belopp):
        if self.start_saldo < belopp or self.täckning == False:
            print("Överföringen misslyckades")
        else: 
            mottagare.start_saldo = mottagare.start_saldo + belopp 
            self.start_saldo = self.start_saldo - belopp 
            return mottagare.start_saldo, self.start_saldo
    def visa_saldo(self): 
        return self.namn, self.start_saldo
    
    def lägg_till_ränta(self, procent):
        self.start_saldo = self.start_saldo * procent 
        return self.start_saldo
        
    def __str__(self):
        return f"Kundens namn: {self.namn}, saldo: {self.start_saldo}"


class Bank(): 
    def __init__(self): 
        pass 



Jess = Bankkund("Jess", 100, True)
Noor = Bankkund('Noor', 1000, True)
Stefan = Bankkund('Stefan', 4206967, False)
Stefans_Fru = Bankkund('Stefans Fru', 98217393874983274903285498327983749, True)

Bankkunder = []
Bankkunder.append(Jess)
Bankkunder.append(Noor)
Bankkunder.append(Stefan)
Bankkunder.append(Stefans_Fru)

Jess.insättning(400)
Jess.lägg_till_ränta(0.2) #idk ill need to fix ts a bit 

for kund in Bankkunder:
    print(kund)  



