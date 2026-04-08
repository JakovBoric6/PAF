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
import matplotlib.pyplot as plt

class Particle: # definiram gibanje projektila
    def __init__(self,pocetna_brzina,kut,p_x=0,p_y=0): #definiram početne uvjete kao atribute u klasi.
       
        self.v0 =pocetna_brzina  
        self.theta_stupnjevi=kut 
        self.theta_radijani=math.radians(kut) #Ovo za kut iz stupnjeva u radijane sam nasao na https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
        self.x0=p_x  
        self.y0=p_y  
        self.g=9.81  
        self.reset()

    def reset(self):

        #rastavljam brzinu na x i y komponentu (t-trenutna)
        self.t_vx= self.v0*math.cos(self.theta_radijani) 
        self.t_vy=self.v0*math.sin(self.theta_radijani) 

        #također definiram i x i y položaj
        self.t_x=self.x0
        self.t_y = self.y0
        
        #(t-trenutno, t-vrijeme)
        self.t_t=0.0

        #ovo su liste u koje cu pohranjivati tocke koje dobivam (#p-putanja) (slicno kao od prethodnih vježbi)
        self.p_x=[self.x0]
        self.p_y=[self.y0]

    def __move(self,dt): #pomicem cesticu za korak u infinitezimalnom dt (Eulerova metoda) ,AI mi je pomogao s formulacijom jednadžbi jer se ne snalazim najbolje s klasama
       
        #(n-nova)
        n_x=self.t_x+self.t_vx*dt
        
        n_y=self.t_y+self.t_vy*dt

        n_vy = self.t_vy-self.g *dt #vy se mijenja s vremenom 

        # Ažuriranje trenutnog stanja cestice
        self.t_x=n_x
        self.t_y=n_y
        self.t_vy= n_vy
        self.t_t +=dt

        #appendam sve svoje nove tocke u liste koje sam već prije definirao
        self.p_x.append(self.t_x)
        self.p_y.append(self.t_y)

    def range(self,dt=0.01):
       #stavljam česticu u pocetno stanje prije pocetka racunanja dometa 
        self.reset()

       
        while self.t_y >= self.y0 or self.t_t==0.0:
            self.__move(dt)
            #moramo uracunati razinu tla!
            if self.t_y < self.y0:
                break
        return self.t_x

    def plot_trajectory(self):
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.p_x, self.p_y, label=f'putanja (v0={self.v0} m/s, θ={self.theta_stupnjevi})')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.title('Putanja čestice')
        plt.grid(True)
        
        plt.show()

    