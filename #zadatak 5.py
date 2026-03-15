#zadatak 5
#Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate unesene koordinate i pravac koji prolazi kroz njih. Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi kao PDF. Dopustite korisniku da bira ime pod kojim će se spremiti graf.

import matplotlib.pyplot as plt
def krivulja(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    print("y=",k,"*x+",l)


print("unesite prvu točku")
x1=float(input("x1="))
y1=float(input("y1="))

print("unesite drugu točku")
x2=float(input("x2="))
y2=float(input("y2="))

xlista=[x1,x2]
ylista=[y1,y2]



plt.plot(xlista,ylista, "ro", label="točke")
plt.plot(xlista,ylista, "b", label="pravac")
plt.legend()
plt.grid(True)
krivulja(x1,y1,x2,y2)


print("Želite li prikazati ovu krivulju kao graf ili spremiti u PDF?")
print("1-prikazuje graf")
print("2-sprema graf u PDF")
odabir=input("Vaš odabir:")
if odabir == "1":
    plt.show()
elif odabir == "2":
     ime_datoteke = input("Unesite ime datoteke: ")
     plt.savefig(ime_datoteke + ".pdf")
     print("Graf je spremljen")

#AI mi je pomogao u dijelu spremanja u pdf i u redoslijedu jer mi je if bio na krivom mjestu jer graf prije mora biti spreman nego što ga pozovem.