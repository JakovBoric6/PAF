import math

g=9.81 
ro=1.225 
Co=0.47 

class Projectile:
    def __init__(self,masa,radius,x0,y0,vx0,vy0):
        self.masa=masa 
        self.radius=radius 
        self.x=x0 
        self.y=y0 
        self.vx=vx0 
        self.vy=vy0 
        self.povrsina= math.pi*(radius**2) 

    #sada definiram funkciju koja ce mi racunati derivacije akceleracije i brzine jer je to potrebno za Runge_Kutt metodu također
    def dobivam_derivacije(self,t_vx,t_vy):
        # Izračun ukupne brzine projektila u trenutnom stanju
        v_ukupno = math.sqrt(t_vx**2+t_vy**2)

        F_otpor_x=0
        F_otpor_y=0


        if v_ukupno > 0: # Ovdje sprječavam dijeljenje s nulom opet
            
            F_otpor_ukupno =0.5*ro*self.povrsina*Co*(v_ukupno**2)

            F_otpor_x=-F_otpor_ukupno*(t_vx /v_ukupno)
            F_otpor_y =-F_otpor_ukupno*(t_vy/v_ukupno)

        F_ukupna_x =F_otpor_x
    
        F_ukupna_y =F_otpor_y-(self.masa * g)

        ax = F_ukupna_x / self.masa
        ay = F_ukupna_y / self.masa

        return ax,ay,t_vx,t_vy

    def _azuriram_poziciju(self, dt): # funkcija za racunanje novih pozicija i brzina ovisno o infinitezimalnom dt
        
        ax,ay,dx_dt,dy_dt=self.dobivam_derivacije(self.vx,self.vy)

        #azuriram svoje brine pomocu akceleracije
        self.vx += ax*dt
        self.vy +=ay*dt
    
        self.x +=dx_dt*dt
        self.y += dy_dt*dt

        #ne smijem dati da moj projektil padne ispod razine zemlje
        if self.y<0:
            self.y=0
            self.vy=0

    #Nova funkcija za azuriranje stanja s Runge-Kutt metodom (kko sam istrazio ona je puno preciznija za vece dt_ove)- formule mi je pojasnio i dao AI
    
    def _azuriram_poziciju_rk4(self,dt): #ovo mi je predlozio i pojasnio AI (priv-privremeno)
        #K1- derivacije na početku intervala
        k1_ax, k1_ay, k1_dx, k1_dy =self.dobivam_derivacije(self.vx,self.vy)

        #K2- derivacije na sredini intervala 
   
        vx_priv_k2 =self.vx+k1_ax*dt/2
        vy_priv_k2 =self.vy+k1_ay*dt/2
        k2_ax, k2_ay, k2_dx, k2_dy =self.dobivam_derivacije(vx_priv_k2,vy_priv_k2)

        #K3- drugi put procjenjujem derivaciju na sredini intervala

        vx_priv_k3 =self.vx+k2_ax*dt/2
        vy_priv_k3 =self.vy+k2_ay*dt /2
        k3_ax, k3_ay, k3_dx, k3_dy =self.dobivam_derivacije(vx_priv_k3,vy_priv_k3)

        #K4-derivacija na kraju intervala 
       
        vx_priv_k4 =self.vx+k3_ax*dt
        vy_priv_k4 =self.vy+k3_ay*dt
        k4_ax, k4_ay, k4_dx, k4_dy = self.dobivam_derivacije(vx_priv_k4, vy_priv_k4)


        self.vx +=(k1_ax + 2*k2_ax + 2*k3_ax +k4_ax)*dt/6
        self.vy +=(k1_ay +2*k2_ay + 2*k3_ay +k4_ay)*dt/6
        self.x +=(k1_dx +2*k2_dx + 2*k3_dx +k4_dx)*dt/6
        self.y +=(k1_dy +2*k2_dy + 2*k3_dy +k4_dy)*dt/6

        #sad opet moram uvesti provjeru da mi projektil ne prođe tlo(0 u koordinatnom sustavu)
        if self.y<0:
            self.y=0
            self.vy=0

    def simulacija_euler(self,dt,vrijeme):
        # ovdje appendam svoje koordinate
        x_putanja=[self.x]
        y_putanja=[self.y]
        poc_t=0 

        while self.y >= 0 and poc_t < vrijeme: #ovdje sam koristio AI
            self._azuriram_poziciju(dt) 

            x_putanja.append(self.x)
            y_putanja.append(self.y)
            poc_t +=dt 
        return x_putanja,y_putanja 






    def simulacija_rk4(self,dt,vrijeme):
        
        x_putanja=[self.x]
        y_putanja=[self.y]
        poc_t=0

        while self.y >= 0 and poc_t < vrijeme:
            self._azuriram_poziciju_rk4(dt) 

            x_putanja.append(self.x)
            y_putanja.append(self.y)
            poc_t += dt 
        return x_putanja, y_putanja 
