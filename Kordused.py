bussi_maht=int(input("Maht: "))#20
k=int(input("Kogus: ")) #110
#busside_arv=k//bussi_maht #100//20=5
jääk=k%bussi_maht #10
if jääk==0:
    busside_arv=k//bussi_maht
else:
    busside_arv=k//bussi_maht+1
print("On vaja ",busside_arv)






#3
from random import *
p=1
for i in range(8):
    a=randint(-10,10)
    print(a)
    if a>0: p*=a
print(p)

#1
print("1. variant")
k=0
mitu=0
while k<15:
    k+=1
    n=float(input("Sisesta arv nr."+str(k)))
    if int(n)==float(n):
        mitu+=1   
print("2. variant")
k=0
mitu=0
while True:
    k+=1
    n=float(input("Sisesta arv nr."+str(k)))
    if int(n)==float(n):
        mitu+=1
    if k==15: break
print("3. variant")
mitu=0
for k in range(1,16):
    n=float(input("Sisesta arv nr."+str(k)))
    if int(n)==float(n):
        mitu+=1
print("Täisarvude kogus: ",mitu)




for i in range(10,0,-2): # 
    print(i)

for i in range(15): # 1 - 14, samm=1
    print(i,"samm")

for i in range(10):
    n=input("Nimi: ")
    print("\tTere",n)


vastus=""
while vastus.lower()!="komm":
    vastus=input("Tahan komme!")

print()
while True:
    vastus=input("Väga tahan komme!")
    if vastus.lower()=="komm":
        break
    else:
        print("Kõik räägivad "+vastus)

print()
while True: #lõpmatu tsükkel
    try:
        pikkus=int(input("Pikkus: "))
        laius=int(input("Laius: "))
        if pikkus>0 and laius>0:
            print("Pindala:",pikkus*laius)
            print("Pikkus ja laius on sisetanud ja pindala on leidnud")
        else:
            print("On vaja andmeid suurem kui 0")
            print("Pikkus ja laius on sisetanud ja pindala ei ole leidnud")
        break
    except :
        print("On vaja int formaat kasutada!") #ilmub ekraanil, kui viga andmetega
print("Töö lõpp")
