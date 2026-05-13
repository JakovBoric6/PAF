import math
import statistics

tocke=[1.5, 2.3, 3.8, 4.2, 5.0, 6.1, 7.4, 8.9, 9.1, 10.5] 
n=len(tocke) 

sredina=statistics.mean(tocke) #koristim ovdje funkciju mean za aritmeticku sredinu

devijacija =statistics.stdev(tocke) #isto za devijaciju da sam htio da se poklapaju rezultati u a i b napisao bi (standardna_devijacija =statistics.stdev(tocke) / math.sqrt(n)) jer je u nasoj formuli u nazivniku definirano n(n-1) a u modulu je samo (n-1)
standardna_devijacija =statistics.stdev(tocke) / math.sqrt(n)

print("Aritmeticka sredina (gotov modul):", sredina)
print("Standardna devijacija (gotov modul):", devijacija)
print("ovo je kad smo malo samostalno popravili modul",standardna_devijacija)
