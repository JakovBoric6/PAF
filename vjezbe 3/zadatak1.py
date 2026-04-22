import math
import matplotlib.pyplot as plt

g=9.81  
ro=1.225 #gustoca zraka
Co=0.47 #koeficijent otpora

class Projectile:
    def __init__(self,masa,radius,x0,y0,vx0,vy0):
        self.masa=masa  
        self.radius=radius  
        self.x=x0  
        self.y=y0  
        self.vx=vx0  
        self.vy=vy0  
        self
        self.povrsina =math.pi*(radius**2)  #racunam povrsinu

    def _azuriram_poziciju(self,dt):
        # funkcija za racunanje novih pozicija i brzina ovisno o infinitezimalnom dt

        v_ukupno =math.sqrt(self.vx**2+self.vy**2)
        F_otpor_x=0
        F_otpor_y=0

        if v_ukupno >0: #ovo je i potrebno da ne bi dijelio s 0
            F_otpor_ukupno=0.5*ro*self.povrsina*Co*(v_ukupno**2) 
            
            #rastavljam silu otpora na komponente...
            F_otpor_x =-F_otpor_ukupno*(self.vx / v_ukupno)
            F_otpor_y =-F_otpor_ukupno*(self.vy / v_ukupno)

        #Ukupne sile na projektil...
        F_ukupna_x = F_otpor_x
        F_ukupna_y = F_otpor_y-(self.masa*g)

        #racunam akceleraciju...
        ax =F_ukupna_x /self.masa
        ay =F_ukupna_y /self.masa

       #sada koristim Eulerove jednadžbe...
        self.vx +=ax*dt
        self.vy +=ay*dt

        self.x +=self.vx*dt
        self.y +=self.vy*dt

        #ovdje uzimam u oobziram da sam postavio koordinatni sustav na nacin da ne smije preci 0(razinu zemlje)
        if self.y <0:
            self.y=0
            self.vy=0

    def simulacija(self,dt,vrijeme):
      #sada radim na putanji (appendam vrijednosti koordinata)
        x_putanja =[self.x] 
        y_putanja =[self.y]
        
        poc_t =0

        while self.y >=0 and poc_t <vrijeme:    #ove mi je uvjete sugerirao AI 
            self._azuriram_poziciju(dt) 
            x_putanja.append(self.x) 
            y_putanja.append(self.y) 
            poc_t +=dt #trenutno vrijeme
            
        return x_putanja,y_putanja #vrati mi moje nove azurirane liste