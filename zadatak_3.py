import calculus
import numpy as np
import matplotlib.pyplot as plt


def kubna_funk(x):
    return x**3-6*x**2+9*x+11
#sada definiram analiticku derivaciju te iste funkcije
def a_der_kubna(x):
    return 3*x**2-12*x+9


def sinus_funk(x):
    return np.sin(x)
#definiram analiticku derivaciju of sinusa
def a_der_sinus(x):
    return np.cos(x)

# tocka kojom cu ih testirati...
test_tocka = 2.0

# prvo cu testirati kubnu funkciju... za nasu proizvoljnu tocku
der_kubna_three_step =calculus.derivacija_u_tocki(kubna_funk,test_tocka,metoda="three-step")
der_kubna_two_step=calculus.derivacija_u_tocki(kubna_funk,test_tocka,metoda="two-step")
a_kubna_vr= a_der_kubna(test_tocka)
print("Kubna funkcija u x je:",test_tocka,)
print("analiticka derivacija:",a_kubna_vr)
print("Nnumericka,three-step:",der_kubna_three_step)
print("numericka.two-step :",der_kubna_two_step)

#a sada sinus
deriv_sin_three_step= calculus.derivacija_u_tocki(sinus_funk, test_tocka,metoda="three-step")
deriv_sin_two_step= calculus.derivacija_u_tocki(sinus_funk,test_tocka, metoda="two-step")
analiticka_sin_vrijednost =a_der_sinus(test_tocka)
print("sinusna funkcija u x je",test_tocka,)
print("analiticka derivacija je" ,analiticka_sin_vrijednost,)
print("numericka. three-step je",deriv_sin_three_step)
print("numericka.two-steo je",deriv_sin_two_step,)

# biram broj tocaka koji zelim i donju i gornju granicu (granice intervala)...
donja_granica_kub=0
gornja_granica_kub=4
br_tocaka=5000

#dobivam podatke za analiticku der
x_vr_kub=np.linspace(donja_granica_kub, gornja_granica_kub, br_tocaka) #x vrijednosti
y_a_kub=a_der_kubna(x_vr_kub) #y analiticka kubna


plt.figure(figsize=(12,8))
plt.plot(x_vr_kub,y_a_kub,label="Analiticka derivacija",color='black',linestyle='--',linewidth=2) 

epsiloni=[0.1,0.01,0.001]
boje_3=['red', 'orange', 'salmon'] #Ai mi je dao boje
boje_2=['blue', 'cyan', 'lightblue']

for i,ep in enumerate(epsiloni):  #AI mi je predlozio ovu metodu s enumerate kako bi istodobno dobro izabrao boju za graf i takoder uzeo epsilone
    #prvo cu za 3 koraka
    x_3,y_3= calculus.derivacija_funcije_u_intervalu(kubna_funk,donja_granica_kub, gornja_granica_kub,tocke=br_tocaka,epsilon=ep,metoda="three-step")
    plt.plot(x_3,y_3,label="Numericka(three-step)",color=boje_3[i])

    #Pa za 2 koraka
    x_2,y_2=calculus.derivacija_funcije_u_intervalu(kubna_funk, donja_granica_kub,gornja_granica_kub,tocke=br_tocaka,epsilon=ep,metoda="two-step")
    plt.plot(x_2,y_2,label="numericka(two-step)",color=boje_2[i])

plt.title("Derivacija kubne funkcije(analiticka i numericka)") 
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)
plt.show()


#opet definiram pocetne uvjete
donja_granica_sin=-4*np.pi
gornja_granica_sin =2*np.pi
br_tocaka=5000

# prvo dajem podatke za analiticku...
x_vr_sin= np.linspace(donja_granica_sin,gornja_granica_sin,br_tocaka)
y_a_sin=a_der_sinus(x_vr_sin)

plt.figure(figsize=(12,8))
plt.plot(x_vr_sin,y_a_sin,label="analiticka",color="black")

epsiloni = [0.1,0.01,0.001]
boje_3 = ['red', 'orange', 'salmon']
boje_2= ['blue', 'cyan', 'lightblue']

for i,ep in enumerate(epsiloni):
    # prvo 3 koraka
    x_3, y_3 =calculus.derivacija_funcije_u_intervalu(sinus_funk,donja_granica_sin,gornja_granica_sin,tocke=br_tocaka,epsilon=ep,metoda="three-step")
    plt.plot(x_3,y_3, label="Numericka(three-step)",color=boje_3[i])

    #za 2 koraka
    x_2,y_2 =calculus.derivacija_funcije_u_intervalu(sinus_funk,donja_granica_sin,gornja_granica_sin,tocke=br_tocaka,epsilon=ep,metoda="two-step")
    plt.plot(x_2,y_2,label="numericka(two-step)",color=boje_2[i])

plt.title("Derivacija sinusne funkcije(analiticka i numericka)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)
plt.show()
