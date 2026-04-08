#Zadatak 4
#U modulu "calculus.py" implementirajte nove dvije metode:
#• Prva metoda kao ulazne parametre prima funkciju, granice integracije i broj podjela za numeričku
#integraciju, a vraća gornju i donju među koristeći pravokutnu aproksimaciju.
#• Druga metoda ima iste ulazne parametre a vraća numeričku vrijednost integrala koristeći trapeznu
#formulu.
#Testirajte modul na primjeru proizvoljno odabrane funkcije i raspona integracije. Neka korisnik u svom
#kodu importa modul calculus i za integraciju koristi gotove metode iz tog modula. Nacrtajte na istom grafu
#analitičko riješenje i numerička riješenja za različiti broj koraka i obe metode numeričke integracije.

import numpy as np

def two_step_derivacija(funkcija, x,epsilon):
    # f'(x)=(f(x+epsilon)-f(x))/epsilon
    return (funkcija(x + epsilon)-funkcija(x)) /epsilon #deinicija

def three_step_derivacija(funkcija, x, epsilon):
    # f'(x)=(f(x+epsilon)-f(x-epsilon))/(2*epsilon)
    return (funkcija(x+epsilon)-funkcija(x-epsilon)) /(2 *epsilon) #definicija koja se rjeđe viđa(tocnija)

def derivacija_u_tocki(funkcija,tocka,epsilon=0.001, metoda='three-step'):
    if metoda=='two-step':
        return two_step_derivacija(funkcija, tocka,epsilon)
    elif metoda=='three-step':
        return three_step_derivacija(funkcija,tocka,epsilon)
    
def derivacija_funcije_u_intervalu(funkcija, donja_granica, gornja_granica, tocke=1000, epsilon=0.001, metoda='three-step'):
    tocke_derivacije = np.linspace(donja_granica, gornja_granica, tocke).tolist()
    derivacije = [derivacija_u_tocki(funkcija,p,epsilon, metoda) for p in tocke_derivacije]
    return tocke_derivacije,derivacije

#ovo sve gore je iz prethodnog koda calculus.py

def pravokutna_integracija(funkcija,a,b,n): #ona nam racuna gornju i donju sumu (Naglašavam kako mi je formulu pri upitu objasnio AI i rekao što ona radi i zašto)
    
    z=(b-a)/n  # Širina svakog mog moguceg intervala
    donja_suma=0
    gornja_suma=0

    for i in range(n):
        x_i =a+i*z
        x_iplus1=a+(i+1)*z  #x_i je lijeva granica a x_iplus1 je desna granica pa na svakoj racunam vrijednosti funkcija

        f_na_x_i=funkcija(x_i)
        f_na_x_iplus1=funkcija(x_iplus1)

        donja_suma +=min(f_na_x_i,f_na_x_iplus1)*z
        gornja_suma +=max(f_na_x_i,f_na_x_iplus1)*z
    return donja_suma,gornja_suma

def trapezna_integracija(funkcija,a,b,n): #daje mi numericku vrijednost (Naglašavam kako mi je nju objasni AI i rekao koja je njezina formula koju sam također provjerio na google)
   
    z=(b-a)/n  # Širina svakog mog moguceg inteevala
    integralna_suma=0.5*(funkcija(a)+funkcija(b)) #a je donja a b gornja granica

    for i in range(1,n):
        integralna_suma +=funkcija(a+i*z) #zbrajam vrijednosti funkcija u svim tockama

    return integralna_suma*z

