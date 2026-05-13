#(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. For
#mula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2.
#(b) Napišite program pod (a) koristeći gotove module.




tocke=[1.5, 2.3, 3.8, 4.2, 5.0, 6.1, 7.4, 8.9, 9.1, 10.5]



ukupno_element=len(tocke) 
zbroj_tocaka=0.0

for x in tocke:
    zbroj_tocaka = zbroj_tocaka+x
 

aritmeticka_sredina= zbroj_tocaka / ukupno_element


#sada krecemo na standardnu devijaciju



zbroj_kvadrata_razlika =0.0

for x in tocke:
    
    razlika = x-aritmeticka_sredina #ovdje gledamo razliku izmedu x i aritmeticke sredine
  
    kvadrat_razlike = razlika**2
    
    zbroj_kvadrata_razlika =zbroj_kvadrata_razlika + kvadrat_razlike


nazivnik = ukupno_element*(ukupno_element-1)


Sve_ispod_korijena = zbroj_kvadrata_razlika / nazivnik


standardna_devijacija = Sve_ispod_korijena**0.5


print("Aritmeticka sredina:",aritmeticka_sredina)
print("Standardna devijacija:",standardna_devijacija)




