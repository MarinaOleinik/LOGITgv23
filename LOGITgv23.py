from random import * #kõik funktsioonid mis on moodulis
#7
a1=randint(1,50)
a2=randint(1,50)
a1=randint(1,50)
a1=randint(1,50)
a1=randint(1,50)




#8
print("@..@".center(10))
print("(----)".center(10))
print("( \__/ )".center(10))
print('^^ "" ^^'.center(10)) 

print("Tere maailm!")
nimi=input("Mis on sinu nimi?")
vanus=int(input("Kui vana sa oled?"))# kommentaar

print("Tere "+nimi+"! Sa oled "+str(vanus)+" aastat vana.") #22!="22"
print("Tere",nimi,"! Sa oled",vanus,"aastat vana.")
print("Tere {0}! Sa oled {1} aasta vana".format(nimi,vanus))

#print(type(nimi))
#print(type(vanus))

arv1=float(input("Arv 1: ")) #3 -> 3.0
t=input("Tehe: ")
arv2=float(input("Arv 2: "))
vastus=eval(str(arv1)+t+str(arv2))
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))

#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print("Muutuja",vanus,"on",type(vanus))
print("Muutuja",eesnimi,"on",type(eesnimi))
print("Muutuja",pikkus,"on",type(pikkus))
print("Muutuja",kas_käib_koolis,"on",type(kas_käib_koolis))

#3

kogus=randint(1,100) #66
print("Kokku on",kogus,"kommid")
mitu=int(input("Mitu kommi tahad võtta?")) #33
kogus=kogus-mitu #kogus=kogus-mitu=66-33  kogus=kogus-mitu->kogus-=mitu
print("Laua peal on",kogus,"kommid")

#4
from math import *
l=float(input("Ümbermõõt: "))
d=round(l/pi,2)          #3.14...
print("Läbimõõt=", d)

