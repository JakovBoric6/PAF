#gibanje-zadatak 2
#Napišite svoj modul "kinematika.py" koji će sadržavati funckiju jednoliko_gibanje(). Neka funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, masa, ...) i neka crta iste grafove kao i u prošlom zadatku. Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati funkciju.

import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje():
    sila=float(input("unesite siliu:"))
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

    vrijeme=[]
    pozicija=[]
    brzina=[]
    lista_akceleracije=[]

    #stavljam pocetne varijable
    x=0
    v=0

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
    plt.title('x/t')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.grid(True)


    plt.subplot(3, 1, 2)  
    plt.plot(vrijeme, brzina, color='green')
    plt.title('v/t')
    plt.xlabel('t')
    plt.ylabel('v')
    plt.grid(True)

    
    plt.subplot(3, 1, 3)  
    plt.plot(vrijeme, lista_akceleracije, color='red')
    plt.title('a/t')
    plt.xlabel('t')
    plt.ylabel('a')
    plt.grid(True)

    plt.tight_layout()  
    plt.show() 
jednoliko_gibanje()

