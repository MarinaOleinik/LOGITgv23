from random import *

nimi=input("Mis on sinu nimi?") #upper()-"JUKU",lower()-"juku",capitalize()-"Juku"
if nimi.upper()=="JUKU":
    print("Lähme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>=120:
        vastus="Viga vanusega"
    elif vanus<6:
        vastus="tasuta pilet"
    elif vanus<14:
        vastus="lastepilet"
    elif vanus<65:
        vastus="täispilet"
    elif vanus<120:
        vastus="sooduspilet"
    print("On vaja Jukule osta",vastus)
else:
    print("Joonistame")







a=randint(-100,200)
if a%2==0:
    print("Juhuslik arv on",a)
    print(a,"-paaris arv")
if a>0:
    print(a,"suurem kui 0")
else:
    print(a,"väiksem kui 0 või võrdne 0-ga")
#a=int(input("Protsent:"))
#<0,>100 ei soobi, 0-59-"2",60-75-"3",76-90-"4",91-100-"5"
if a<0 or a>100:
    print("Viga tulemustega!")
elif a>=0 and a<60:
    print("Hinne 2")
elif a>=60 and a<76:
    print("Hinne 3")
elif a>=76 and a<91:
    print("Hinne 4")
else:
    print("Hinne 5")