#Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5.
#Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.

def racun_trecine(N):
    broj=5.0
    
    for i in range(N):
        broj=broj+(1/3)
        
    for i in range(N):
        broj=broj-(1/3)
        
    return broj

iteracije =[200,2000,20000]

for n in iteracije:
    rez=racun_trecine(n)
    print("Za",n,"iteracija je:", rez)

# razlika u rezultatu se dogodi zato sto racunalo koristi pomicni zarez za decimalne brojeve
# 1/3 se u binarnom sustavu (baza 2) ne moze prikazat savrseno vec se beskonacno ponavlja (0.333333...)
# kompjuter mora negdje to zaustaviti i zaokruziti na neki odredeni broj bitova.
# to nam se u zavrsnom rezultatu vidi kao pogreška, logicno sto imamo više racunanja to ce se sve vise tih malih pogresaka akumulirati i nastati ce veca razlika od pravog rjesenja i onog sto nam program izbaci
#kako raste N tako raste i pogreska