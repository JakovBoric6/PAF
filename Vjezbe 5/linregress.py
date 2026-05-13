#Napišite program linregress.py za određivanje modula torzije Dt aluminijske šipke ako znamo da vrijedi
#M=Dt·φ. Parametri su nam zadani kao M = [0.052,0.124,0.168,0.236,0.284,0.336] Nm,
#φ = [0.1745,0.3491,0.5236,0.6981,0.8727,1.0472] rad. Formule koje možete iskoristiti za doći do grafa
#linearne regresije su:

import matplotlib.pyplot as plt
import math


fi=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]

n=len(fi) #broj nasih mjerenja


suma_xy=0.0
suma_x2=0.0
suma_y2=0.0

for i in range(n):
    x =fi[i]
    y =M[i]

    suma_xy +=x*y
    suma_x2 +=x**2
    suma_y2 +=y**2

#sad samo racunamo srednju vrijednost
s_v_xy =suma_xy/n
s_v_x2 =suma_x2/n
s_v_y2 =suma_y2/n

#racunam modul nagiba i torzije
a =s_v_xy/s_v_x2
Dt=a

#racunam pogresku nagiba
izraz_pod_korijenom =(1/n)*(
    (s_v_y2/s_v_x2)-a**2
)
sigma_a=math.sqrt(izraz_pod_korijenom)

print("Modul torzije Dt (nagib a):",Dt)
print("Standardna pogreska sigma_a:",sigma_a)

      
#crtanje pravca
#p-pravac
plt.figure(figsize=(8, 6))
plt.scatter(fi, M, color="blue", label="Mjerenja", zorder=5)
x_p = [0, max(fi)]
y_p = [Dt*x for x in x_p]
plt.plot(x_p,y_p,color="red",linestyle="--")
plt.xlabel("fi")
plt.ylabel("M")
plt.title("Graf linearne regresije")
plt.grid(True, linestyle=":")
plt.legend()
plt.show()