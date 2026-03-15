#zadatak 3
#Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.
print ("unesite prvu tocku:")
x1=input("x1=")
y1=input("y1=")

while True:
    try:
        x1=float(x1)
        y1=float(y1)
        break
    except:
        print("krivo je, molim vas ponovite:")
        x1=input("x1=")
        y1=input("y1=")

print ("unesite drugu tocku:")
x2=input("x2=")
y2=input("y2=")
while True:
    try:
        x2=float(x2)
        y2=float(y2)
        if x2==x1:
            print("x2 ne smije biti isti kao x1, molim vas ponovite")
            x2=input("x2=")
            y2=input("y2=")
            continue
        break
    except:
        print("krivo je, molim vas ponovite:")
        x2=input("x2=")
        y2=input("y2=")
k=(y2-y1)/(x2-x1)
l=y1-k*x1
print("y=",k,"*x+",l)

# AI mi je napomenuo da postoje naredbe try i except za testirati varijable te sam ih onda upotrijebio kako bi lako testirao je li korisnik unio broj ili ne (može li ga python pretovriti u broj(integer))



