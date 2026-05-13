#(a) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? Koji rezultat dobijete koristeći Python? Objasnite.
#(b) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. Objasnite rezultat koji ste dobili.


rezultat =5.0-4.935   #ocekujem 0.065, a k0risteci python dobijem jako slican ali ne identican broj
print("Rezultat je:",rezultat)

suma=0.1+0.2+0.3
print ("Suma 0.1+0.2+0.3 je:",suma)
print ("Je li 0.1+0.2+0.3 jednako 0.6?",suma==0.6)
#0.1, 0.2 i 0.3 i opcenito decimalni brojevi nemaju sasvim tocnu binarnu reprezentaciju pa se zapravo svaki od njih pohranjuje u programu kao nevjerojatno bliska binarna aproksimacija. zapravo je ovo problem cjelovitog binarnog sustava tj nacina na koji nase racunalo sprema brojeve. zato i ova izravna usporedba u mom kodu daje false jer nisu savrseno identicni rezultati koje dobijemo vec dobijemo nesto neizmjerno blizu.