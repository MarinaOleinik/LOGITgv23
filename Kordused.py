from datetime import *
from random import *
L=10
H=14
for j in range(H):
    for i in range(L):
        print(f"{randint(-10,100):4}",end=" ")
    print()

print()
while True:
    try:
        a=int(input("Mitu tk: "))
        if 0<a<10:
            break
    except ValueError:
        print("Viga. Sisesta arv 1-9!")
for i in range(a):
    print("****")


#Praktiline töö
#Ülesanne 5
for i in range(1,11):
    for j in range(1,11):
        print(f"0",end="")
    print()
#Ülesanne 4
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
#Ülesanne 3
k=0
while True:
    k+=1
    print(f"{k}. ülesanne")
    a=randint(1,50)
    b=randint(1,50)
    p=5
    while True:
        v=int(input(f"{a}+{b}= "))
        p-=1
        if v==a+b:
            print("Õige vastus!")
            break
        elif p==0:
            print(f"{a}+{b}={a+b}")
            break
    if k==10: break





#Ülesanne 2.2 sõne lõpeb tsükkel
sum_=0
i=0
while True:
    i+=1
    arv=input("2.2 Sisesta arv: ")
    if i>10: break
    try:
        arv=int(arv)
        sum_+=arv
    except:
        break
if sum_!=0:
    print(f"Summa= {sum_}")

#Ülesanne 2.1 arv 777 lõpeb tsükkel
sum_=0
i=0
while True:
    i+=1
    arv=int(input("2.1 Sisesta arv: "))
    if i>10: break
    if arv==777: break
    sum_+=arv
print(f"Summa= {sum_}")


#Ülesanne 2
sum_=0
for i in range(10):
    arv=int(input("Sisesta arv: "))
    sum_+=arv
print(f"Summa= {sum_}")



#Ülesanne 1
nimi=input("Palun sisesta oma nimi:")
mitu=int(input("Mitu korda tervitada? "))
for i in range(mitu):
    print(f"Ole tervitatud, {nimi}, {i+1}. korda.")






#8 Poes
arve_nr= date.today()#datetime.now()
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

tooded=["Piim","Leib","Kommid","Või"] #len(tooded)=4
hinnad=[randint(50,150)/100,randint(50,150)/100,randint(100,1500)/100,randint(120,550)/100]
for i in range(len(tooded)): #tooded[0]="Piim, tooded[1]="Leib", tooded[2]="Kommid"
    toode=tooded[i]
    hind=hinnad[i]
    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu?"))
        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
        summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)





bussi_maht=int(input("Maht: "))#20
k=int(input("Kogus: ")) #110
busside_arv=k/bussi_maht
if busside_arv!=int(busside_arv):
    busside_arv+=1


#busside_arv=k//bussi_maht #100//20=5

#jääk=k%bussi_maht #10
#if jääk==0:
#    busside_arv=k//bussi_maht
#else:
#    busside_arv=k//bussi_maht+1
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
