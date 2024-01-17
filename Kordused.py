#1
mitu=0
for k in range(1,6):
    n=float(input("Sisesta "+str(k)+". arv"))
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
