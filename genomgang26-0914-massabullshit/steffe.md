# GENOMGÅNG - 2026 - 09/14

``` py 
``` 


Uppgift: Skapa en Python-klass som heter Bok. Denna klass ska hantera information om böcker och implementera de följande funktionerna. 

Steg 1: Grundläggande Klassstruktur 
    Definiera en klass Bok. 
    I __init__-()metoden, initiera minst tre instansvariabler: titel, författare och utgivningsår. 
    Implementera __str__()-metoden så att den returnerar en tydlig textbeskrivning av bokobjektet (t.ex. "Titel: The Lord of the Rings, Författare: J.R.R. Tolkien"). 

Steg 2: Klassvariabler och Spårning 
Lägg till en klassvariabel, antal_böcker, som tillhör hela klassen. Initialisera den till 0. 
I __init__()-metoden, se till att antal_böcker ökar med 1 varje gång en ny Bok-instans skapas. 
    Lägg till en klassvariabel _hemlig_kod (med ett enkelt understreck) och en __hemligaste_kod (med dubbla understreck). Initialisera båda till 0. 

Steg 3: Klassmetod (@classmethod) 
    Skapa en klassmetod med @classmethod som heter visa_antal_böcker(). 
    Denna metod ska returnera en sträng som tydligt anger det totala antalet böcker som har skapats. Använd klassvariabeln antal_böcker. 

Steg 4: Statisk metod (@staticmethod) 
    Skapa en statisk metod med @staticmethod som heter är_gammal_bok(år). 
    Denna metod ska ta ett heltal som argument, år. 
    Den ska returnera True om året är äldre än 1900, annars False. Denna metod ska inte använda några klass- eller instansvariabler. 



Steg 5: Testa din klass och förstå 'private' 
    Skapa minst tre instanser av din Bok-klass, t.ex. bok1, bok2 och bok3. 
Anropa din klassmetod visa_antal_böcker() för att bekräfta att den returnerar det förväntade antalet. 
Anropa din statiska metod är_gammal_bok() med olika årtal för att testa den. 
Försök att skriva ut värdet på Bok._hemlig_kod. Reflektera över varför detta fungerar. 
 Försök att skriva ut värdet på Bok.__hemligaste_kod. Reflektera över varför detta inte fungerar som förväntat och vad som händer istället. 
Slutligen, skriv ut Bok._Bok__hemligaste_kod för att visa hur man faktiskt kommer åt den "namngenererade" privata variabeln. 


