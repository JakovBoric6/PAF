#zadatak 4
#Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. Neka ta funkcija na ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu.

def krivulja():
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
krivulja()


#AI mi je objasnio pogrešku jer sam prije bio definirao l nego k pa program nije radio te sam samo obrnio radnje.