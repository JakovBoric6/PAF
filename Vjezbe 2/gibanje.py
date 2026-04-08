#Zadatak 1
#U zasebnom modulu "particle.py" definirajte klasu Particle za čestice koja će imati atribute početne brzine,
#kuta otklona i koordinata početnog položaja. Neka klasa sadrži i sljedeće metode:
#• metodu reset() koja briše sve informacije o čestici
#• privatnu metodu __move() koja pomiče česticu za korak ∆t
#• metodu range() koja numerički računa domet projektila
#• metodu plot_trajectory() koja crta putanju u x − y ravnini za trenutno stanje čestice.
#Koristeći klasu Particle u programu "gibanje.py" kreirajte jednan objekt i postavite ga na neke od vrijednosti
#za koje ste analitički izračunali domet. Da li se numeričko riješenje slaže s analitičkim? Koliko je odstupanje?

import math
from particle import Particle # Sada uvozimo klasu iz datoteke particle.py
import matplotlib.pyplot as plt 

# analiticki pristup dometu
def i_analiticki_domet(v0,kut_stupnjevi,g=9.81):
   
    kut_radijani =math.radians(kut_stupnjevi)
    #formula: R=(v0^2 * sin(2*theta)) / g
    return (v0**2*math.sin(2*kut_radijani))/g

# provjerio sam analitički rezultat... (uzimam proizvoljne vrijednosti)
p_v=50.0  
kut=45.0 
p_x=0.0 
p_y=0.0 
infinitezimalni_dio=0.01 

#KStvaranje čestice
projektil=Particle(p_v,kut,p_x,p_y)

numericki_domet= projektil.range(dt=infinitezimalni_dio)

analiticki_domet=i_analiticki_domet(p_v, kut)

#Usporedba i odstupanje  
odstupanje=abs(numericki_domet - analiticki_domet)
postotno_odstupanje = (odstupanje / analiticki_domet) * 100 if analiticki_domet != 0 else 0 #AI mi je napomenuo da bi mogao staviti pvaj uvjet else 0

#printanje svih informacija...
print ( "Numericki domet:",numericki_domet, "m")
print("Analiticki domet:",analiticki_domet,"m")
print("Odstupanje između numerickog i analitickog:",odstupanje,"m")
print("odstupanje u postotku:",postotno_odstupanje,"%")

projektil.plot_trajectory()
