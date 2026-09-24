import random 

class Bankkund():
    def __init__(self, namn, start_saldo, täckning, kreditgräns = 5000):
        self.namn = namn
        self.start_saldo = start_saldo 
        self.täckning = täckning 
        self.kreditgräns = kreditgräns 
        self.kontonummer = random.randint(1000000, 9999999)
        self.historik = []
        self.historik.append(f"Konto skapat, med saldo: {start_saldo}")

    
    def insättning(self, belopp):
        if belopp < 0 or self.täckning == False: 
            print("Transaktionen misslyckades")
        else:
            self.start_saldo = self.start_saldo + belopp  
            self.historik.append(f"Insättning: +{belopp}. Nytt saldo: {self.start_saldo}")
            return self.start_saldo 
    def uttag(self, belopp):
        if (self.start_saldo - belopp) < -self.kreditgräns or belopp <= 0 or self.täckning == False: 
            print("Transaktionen misslyckades")
        else: 
            self.start_saldo = self.start_saldo - belopp 
            self.historik.append(f"Uttag: -{belopp}. Nytt saldo: {self.start_saldo}")
            return self.start_saldo 
    def överföring(self, mottagare, belopp):
        if (self.start_saldo - belopp) < -self.kreditgräns or belopp <= 0 or self.täckning == False:
            print("Överföringen misslyckades")
        else: 
            mottagare.start_saldo = mottagare.start_saldo + belopp 
            self.start_saldo = self.start_saldo - belopp 
            self.historik.append(f"Överföring: -{belopp} till {mottagare.namn}")
            self.historik.append(f"Mottaget: {belopp} från {self.namn}")
            return mottagare.start_saldo, self.start_saldo
    def visa_saldo(self): 
        return self.namn, self.start_saldo
    
    def lägg_till_ränta(self, procent):
        ökning = self.start_saldo * procent 
        self.start_saldo += ökning
        self.historik.append(f"Ränta pålagd med {procent*100}%, nytt saldo = {self.start_saldo}")
        return self.start_saldo
    def visa_transaktioner(self):
        print(f"\n Transaktionshistorik för {self.namn}")
        for transaktion in self.historik: 
            print(transaktion)
        
    def __str__(self):
        return f"Kundens namn: {self.namn}, kontonummer: {self.kontonummer} saldo: {self.start_saldo}"


class Bank(): 
    def __init__(self): 
        self.kunder = []
    def lägg_till_kund(self, kund): 
        self.kunder.append(kund)
    def totalt_saldo(self): 
        totalt = 0
        for kund in self.kunder: 
            totalt += kund.start_saldo
        return totalt 
    def hitta_kund(self, sökord):
        for kund in self.kunder:
            if kund.namn.lower()== str(sökord).lower() or str(kund.kontonummer) == str(sökord):
              return kund 
        return None   


a_bank = Bank()


Jess = Bankkund("Jess", 100, True)
Noor = Bankkund('Noor', 1000, True)
Stefan = Bankkund('Stefan', 4206967, False)
Stefans_Fru = Bankkund('Stefans Fru', 98217393874983274903285498327983749, True)

Bankkunder = []
Bankkunder.append(Jess)
Bankkunder.append(Noor)
Bankkunder.append(Stefan)
Bankkunder.append(Stefans_Fru)

a_bank.lägg_till_kund(Jess)
a_bank.lägg_till_kund(Noor)
a_bank.lägg_till_kund(Stefan)
a_bank.lägg_till_kund(Stefans_Fru)


Noor.insättning(400) #testing 
Jess.lägg_till_ränta(0.2) #idk ill need to fix ts a bit 
Jess.uttag(2000)
Jess.överföring(Noor, 100)

Jess.visa_transaktioner()
Noor.visa_transaktioner()

print(f"\nTotalt saldo  i hela banken: {a_bank.totalt_saldo()}")

hittad = a_bank.hitta_kund('Noor')
if hittad: 
    print(f"\nHittade kund via sökning: {hittad}")

""" for kund in Bankkunder:
    print(kund) """  



