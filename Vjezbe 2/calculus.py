#Napišite modul "calculus.py" koji će sadržavati dvije metode:
#• Prva metoda kao ulazne parametre prima funkciju i točku, a kao rezultat vraća vrijednost derivacije
#funkcije u toj točki.
#• Druga prima kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije. Funkcija
#korisniku vraća listu točaka u kojima će biti izvršena numerička derivacija na zadanom rasponu i
#iznose derivacije funkcije u tim istim točkama.
#Testirajte modul na primjerima kubne i trigonometrijske funkcije. Neka korisnik u svom kodu importa
#modul calculus i za derivaciju koristi gotove metode iz tog modula. Nacrtajte na istom grafu analitičko
#rješenje i numerička rješenja za različite korake numeričke derivacije. To ćete postići tako da u razvijenim
#metodama iz modula calculus dodate opciju da metoda kao jedan od ulaznih parametara prima i veličinu
#koraka derivacije ϵ i metodu kojom derivira. Neka "three-step" metoda bude zadana ako korisnik ništa ne
#odabere, a "two-step" metoda bude druga ponuđena opcija.

import numpy as np

def two_step_derivacija(funkcija,x,epsilon):
    
    #f'(x)=(f(x+epsilon)-f(x))/epsilon - ovu mi je formulu dao AI i Google
    
    return (funkcija(x+epsilon)-funkcija(x))/epsilon

def three_step_derivacija(funkcija,x,epsilon):
    
    #f'(x)=(f(x+epsilon)-f(x-epsilon))/(2*epsilon)- ovu mi je formulu dao AI i Google
    
    return (funkcija(x+epsilon)-funkcija(x-epsilon))/(2*epsilon)

def derivacija_u_tocki(funkcija,tocka,epsilon=0.001,metoda='three-step'):
   
    if metoda=='two-step':
        return two_step_derivacija(funkcija,tocka,epsilon)
    elif metoda=='three-step':
        return three_step_derivacija(funkcija,tocka,epsilon)
    
def derivacija_funcije_u_intervalu(funkcija,donja_granica,gornja_granica,tocke=1000,epsilon=0.001,metoda='three-step'):
   
    tocke = np.linspace(donja_granica,gornja_granica,tocke).tolist() #ovaj dio koda mi je pomogao AI kako bi koherentno spremio tocke i derivacije u listu
    derivacije = [derivacija_u_tocki(funkcija, p,epsilon,metoda) for p in tocke]
    return tocke, derivacije