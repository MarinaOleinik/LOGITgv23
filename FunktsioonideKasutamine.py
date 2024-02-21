from MyModul import *
from random import *
p=21
k=2
a=2024
t=date_(5,5,2005)
print(t)

#(6)
arv=int(input("Sisesta arv: "))
if is_prime(arv):
    print("Lihtne arv")
else:
    print("Liitarv")

#(5)
summa=float(input("Summa: "))
aastad=int(input("Aastad: "))
summa=bank(summa,aastad)
print(f"{aastad} aasta pärast summa on {summa}")

#(4)
nr=int(input("Kuu järjekorranumber: "))
vastus=season(nr)
print(vastus)


#(3)
a=float(input("Ruudukülg:"))
S,P,D=square(a)
print("S=",S)
print("P=",P)
print("D=",D)
#(2)
for i in range(5):
    aasta=randint(1900,2200)
    if is_year_leap(aasta):
        print(f"Aasta {aasta} on liigaasta")
    else:
        print(f"Aasta {aasta} on tavaline")


#(1)
a=int(input("Arv1: "))
t=input("Tehe: ")
b=int(input("Arv2: "))
vastus=arithmetic(a,t,b)
print(f"{a}{t}{b}=",vastus,sep="")

#1
summa_3=Summa(5,8,12)
print(summa_3)
#2
a=float(input("Arv1: "))
b=float(input("Arv2: "))
summa_3=Summa(a,b)
print(summa_3)
#3
summa_3=Summa(
    float(input("Arv1: ")),
    float(input("Arv2: ")),
    float(input("Arv3: ")))
print(summa_3)
