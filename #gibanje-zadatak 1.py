#gibanje-zadatak 1
#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np #iz nekog razloga mi numpy ne funkcionira u vscode te sam kod testirao u google colabu gdje je radio"
import matplotlib.pyplot as plt
sila=float(input("unesite iznos sile:"))
masa=float(input("unesite masu:"))
if masa==0:
    print("masa ne može biti 0, upišite novu vrijednost mase:")
    masa=float(input("unesite masu:"))
else:
    akceleracija= sila/masa
    print("akceleracija je:", akceleracija,"m/s2")

vrijeme_p=0
vrijeme_k=10
dt=0.01
#istazio sam numericko rjesavanje i nasao kako je najlakse rijesiti pomocu apendanja podataka koje dobijem petljom.
vrijeme=[]
pozicija=[]
brzina=[]
lista_akceleracije=[]

#stavljam pocetne varijable
x=0
v=0

#AI mi je otkrio Eulerovu metodu za rješavanje diferencijalnih jednadžbi te dao kod koji sam prilagodio zadatku.
for t in np.arange(vrijeme_p, vrijeme_k + dt, dt):
        vrijeme.append(t)
        pozicija.append(x)
        brzina.append(v)
        lista_akceleracije.append(akceleracija)

#obicne jednadzbe s infinitezimalnim pomakom ("moraju biti u petlji! ")
        x = x + v * dt 
        v = v + akceleracija * dt

plt.figure(figsize=(12, 10)) #podešavanje okvira za slike- našao na https://www.geeksforgeeks.org/

plt.subplot(3, 1, 1)  
plt.plot(vrijeme, pozicija, color='blue')
plt.title('x-t')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid(True)


plt.subplot(3, 1, 2)  
plt.plot(vrijeme, brzina, color='green')
plt.title('v-t')
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')
plt.grid(True)

    
plt.subplot(3, 1, 3)  
plt.plot(vrijeme, lista_akceleracije, color='red')
plt.title('a-t')
plt.xlabel('t (s)')
plt.ylabel('a (m/s2)')
plt.grid(True)

plt.tight_layout()  
plt.show()

#za grafove sam nasao kod na internetu na https://www.geeksforgeeks.org/ te ga napravio 3 puta za 3 tražena grafa