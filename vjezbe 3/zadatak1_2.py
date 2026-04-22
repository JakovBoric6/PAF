
import math
import matplotlib.pyplot as plt
from zadatak1 import Projectile

g=9.81  
ro=1.225 #gustoca zraka
Co=0.47 #koeficijent otpora


#definiram pocetne uvjete
masa =0.1 
radius=0.05
poc_x =0
poc_y =0
poc_v =50
kut= 45 

kut_rad =math.radians(kut) #AI predložio

poc_vx = poc_v*math.cos(kut_rad)
poc_vy = poc_v* math.sin(kut_rad)


dt_vr=[0.5, 0.1, 0.05, 0.01, 0.005, 0.001] #Ai mi je predlozio kakve korake da uzmem da graf pokaže bolje bit
vrijeme= 20 






plt.figure(figsize=(12, 8)) 

for dt in dt_vr:

    Projectile2 = Projectile(masa,radius,poc_x,poc_y,poc_vx,poc_vy)
    
    x_t, y_t = Projectile2.simulacija(dt,vrijeme)
    
    plt.plot(x_t, y_t,)

plt.xlabel('Horizontalna udaljenost')
plt.ylabel('Vertikalna udaljenost')
plt.title("Putanja projektila sa otporom zraka za drugacije dt-ove")
plt.grid(True)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8) #dao mi je AI za bolji prikaz vise linija na grafu
plt.show()