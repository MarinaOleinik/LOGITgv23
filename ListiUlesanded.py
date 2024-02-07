#2
from audioop import avg


nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ")
    nimed.append(nimi)

print("Sisestatud: ",nimed)
nimed.sort()
print("Sorteeritud: ",nimed)
print("Vimasena oli lisatud: ",nimi)
nimi=input("Mis nimi on vaja asendada? ")#!!! Kodus
#indeks=nimed.index(nimi)
uus_nimi=input("Uus nimi: ")
#nimed[indeks]=uus_nimi
nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
nimed=set(nimed)#!!! Kodus
print(nimed)
vanused=[]
for i in range(5):
    v=int(input("Vanus: "))
    vanused.append(v)
sum_=sum(vanused)
min_=min(vanused)
max_=max(vanused)
kesk=avg(vanused)
print("Kesknime on {kesk}, \nSuurim on {max_}, \nVäiksem on {min_}, \nSumma on {sum_}")

#1
from string import *
vokaali=["a","u","i","o","e","ü","ä","ö","õ","y"]
konsonanti="qwrtpsdfghklzxcvbnmj"
märgid=punctuation
v=k=m=t=0
tekst=input("Sisesta tekst: ") #"mama"
print(tekst)
tekst_list=list(tekst) #["m","a","m","a"]
print(tekst_list)
for element in tekst_list:
    if element.lower() in vokaali:
        v+=1
    elif element.lower() in konsonanti:
        k+=1
    elif element in märgid:
        m+=1
    elif element==" ":
        t+=1
print("Vokaali:",v)
print("Konsonanti:",k)
print("Märgid:",m)
print("Tühikud:",t)