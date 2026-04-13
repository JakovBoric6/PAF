#Zadatak 4
#U modulu "calculus.py" implementirajte nove dvije metode:
#• Prva metoda kao ulazne parametre prima funkciju, granice integracije i broj podjela za numeričku
#integraciju, a vraća gornju i donju među koristeći pravokutnu aproksimaciju.
#• Druga metoda ima iste ulazne parametre a vraća numeričku vrijednost integrala koristeći trapeznu
#formulu.
#Testirajte modul na primjeru proizvoljno odabrane funkcije i raspona integracije. Neka korisnik u svom
#kodu importa modul calculus i za integraciju koristi gotove metode iz tog modula. Nacrtajte na istom grafu
#analitičko riješenje i numerička riješenja za različiti broj koraka i obe metode numeričke integracije.

import matplotlib.pyplot as plt
import calculus2

#prvo definiram svoju funkciju (odabrao sam jednostavni x**2 jer za njega je lagani integral x**3 /3)
def test_funkcija(x):
    return x**2
#uzimam neke proizvoljne granice integracije
a=0
b=2

#prvo izracunam analiticki
analiticko_rjes =(b**3/3)-(a**3/3)
print("analitičko rjesenje za integral x**2 od ",a, "do" ,b," je:" ,analiticko_rjes,)

# 4. stavljam razlicite podjele kako bi ih imao za numericko , ovo s podjelama je dobro predlozeno na https://stackoverflow.com/search?q=%5Bpython%5D+numerical+integration&s=6bf56f75-9935-414c-a7af-67a2047054ba
podjele=range(1,1000, 10)
#definiram liste u koje cu stavljati rezultate koje edobivam za svku od podjela!
donja_međa_rez=[] #Donju i gornju među skupljam kao rezultate pravokutne aproksimacije!
gornja_međa_rez=[]
trapezoidni_rez=[] #numericka metoda koju trebam također spremati Napomena:Ovo mi je rekao AI, ja sam prvobitno zaboravio da moram zabilježiti i ove rezultate.

for n in podjele:
    
    donja_međa, gornja_međa =calculus2.pravokutna_integracija(test_funkcija,a,b,n) #važan je redoslijed 
    donja_međa_rez.append(donja_međa)
    gornja_međa_rez.append(gornja_međa)

    # Trapezna formula
    trapez_vr=calculus2.trapezna_integracija(test_funkcija, a, b, n) 
    trapezoidni_rez.append(trapez_vr)

print("Rezultati numericke integracije za različit broj podjela:")
for i, n in enumerate(podjele):
    print("Donja međa:",donja_međa_rez[i],"Gornja međa:",gornja_međa_rez[i],"trapezna aproximacija:" ,trapezoidni_rez[i],)

#crtanje grafova (koristio sam AI kako bi mi on "uljepšao" grafove s bojama drugacijim stilovima i tockama)
plt.figure(figsize=(10,6))
plt.plot(podjele,[analiticko_rjes]*len(podjele),label='Analiticko rjesenje', color='red', linestyle='--') # podjele,[analiticko_rjes]*len(podjele) ovaj dio je bitan jer za svaku tocku moram imati x i y a ovaj kod to omogucava tako sto moju vrijednost mnozi koliko god je potrebno
plt.plot(podjele,donja_međa_rez, label='Pravokutna integracija(donja međa)', marker='o', linestyle='-')
plt.plot(podjele,gornja_međa_rez, label='Pravokutna integracija(gornja međa)', marker='x', linestyle='-')
plt.plot(podjele,trapezoidni_rez, label='Trapezna integracija', marker='s', linestyle='-')

plt.xlabel('broj podjela')
plt.ylabel('Vrijednost integrala')
plt.legend()
plt.grid(True)
plt.show()
