class Bankkund():
    def __init__(self, namn, start_saldo):
        self.namn = namn
        self.start_saldo = start_saldo 
    
    def insättning(self, belopp):
        if belopp < 0: 
            print("brur var fick du negativa pengar ifrån?")
        else:
            self.start_saldo = self.start_saldo + belopp  
            return self.start_saldo 
    def uttag(self, belopp):
        if self.start_saldo < belopp or belopp < 0: 
            print("överföringen misslyckades")
        else: 
            self.start_saldo = self.start_saldo - belopp 
            return self.start_saldo 
    def överföring(self, mottagare, belopp):
        if self.start_saldo < belopp:
            print("youre not that rich bro")
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

Jess = Bankkund("Jess", 100)
Noor = Bankkund('Noor', 1000)
Stefan = Bankkund('Stefan', 4206967)
Stefans_Fru = Bankkund('Stefans Fru', 98217393874983274903285498327983749)

Bankkunder = []
Bankkunder.append(Jess)
Bankkunder.append(Noor)
Bankkunder.append(Stefan)
Bankkunder.append(Stefans_Fru)

for kund in Bankkunder:
    print(kund)  



