import math
import matplotlib.pyplot as plt
from zadatak2 import Projectile
masa=0.1
radius=0.05
x0=0 
y0=0 
v_pocetna=100 
kut=45 

kut_rad = math.radians(kut)

#racunam komponente pocetne brzine
vx0 =v_pocetna*math.cos(kut_rad)
vy0 =v_pocetna*math.sin(kut_rad)


dt = 0.01
vrijeme =20 

#vrlo je žazno da za oba stavimo iste pocetne uvjete ipak ih uspoređujemo
projektil_euler =Projectile(masa, radius, x0, y0,vx0, vy0)
projektil_rk4 =Projectile(masa, radius, x0,y0, vx0,vy0)


#prvo cu Eulera
x_euler,y_euler =projektil_euler.simulacija_euler(dt,vrijeme)


#pa sada drugu metodu
x_rk4,y_rk4 =projektil_rk4.simulacija_rk4(dt,vrijeme)



plt.figure(figsize=(12, 7)) 
plt.plot(x_euler, y_euler, label='Eulerova metoda', linestyle='--', color='blue') 
plt.plot(x_rk4, y_rk4, label='Runge-Kutta 4. reda', color='red')

plt.title("Usporedba putanja za: Euler i Runge-Kutta metode") 
plt.xlabel("Domet") 
plt.ylabel("h") 
plt.grid(True) 
plt.legend() 
plt.show()