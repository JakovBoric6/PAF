#Za česticu početne brzine v0 = 10ms i kuta otklona θ = 60o nacrtajte graf ovisnosti relativne pogreške
#numeričkog riješenja o vrijednosti vremenskog koraka ∆t.

import numpy as np
import matplotlib.pyplot as plt
from particle import Particle 
import math 

def i_analiticki_domet(v0,kut_stupnjevi,g=9.81): #ovdje opet definiram isto što i u prošlom kodu kako bi ga mogao uzeti kao varijablu
   
    kut_radijani =math.radians(kut_stupnjevi)
    #formula:R=(v0^2 *sin(2*theta))/g 
    return (v0**2*math.sin(2*kut_radijani))/g

# definiram pocetne vrijednosti
v0= 10.0  
kut=60.0 
p_x=0.0
p_y=0.0

# Analitički domet 
analiticki_domet1= i_analiticki_domet(v0,kut)

#definiram infinitezimalni element pomocu logaritamske skale (mogu podesiti broj tocaka koji hocu)
dt_vrijednosti=np.linspace (0.0001, 0.1, 1000)

relativna_pogrjeska=[] #u ovu listu u appendati pogreske koje dobijem

# racunam relativnu pogresku za svki dt
for dt in dt_vrijednosti:
    projektil_analiza=Particle(v0,kut,p_x,p_y)
    numericki_domet1=projektil_analiza.range(dt=dt) #ovaj dio dt=dt mi je objasnio AI te razlog zašto ne smijem uvrstiti samo dt zbog nacina na koji python to čita

    #racunam relativnu pogresku
    if analiticki_domet1 !=0:
        pogreska =abs(numericki_domet1-analiticki_domet1)/analiticki_domet1 #formula za relativnu pogresku
        relativna_pogrjeska.append(pogreska)
    else:
        relativna_pogrjeska.append(float('inf'))  # beskonacno velika pogreska jer je nemam s cim usporediti


plt.figure()
plt.plot(dt_vrijednosti,relativna_pogrjeska) 
plt.xlabel('t (s)')
plt.ylabel('relativna pogreška')
plt.title('ovisnost relativne pogreške o dt')
plt.grid(True)
plt.show()

