from random import *
nimed=["Kadri","Mirje","Maadis","Linda","Kadri"]
while True:
    print("---------------------")
    v=input("N-andmeta näitamine\nL-andmete lisamine\nK-andmete kustutamine\nS-andmete sorteerimine\nE-andmete eemaldamine\nP-andmete pööramine\nC-andmete kopeerimine\nI-indeksi otsing\n").upper()
    if v=="N":
        v=input("Kas kõik?(k) või Juhuslik nimi?(j)").lower()
        if v=="k":
            print(nimed)
        elif v=="j":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas lõppu?(l) või positsioonile?(p)").lower()
        if v=="l":
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Sisesta nimi: ")
            indeks=int(input("Mis positsioonile: "))
            nimed.insert(indeks-1,nimi)
    elif v=="K":
        v=input("Nimi järgi?(n) või järjekorranumbri järgi(j)")
        if v=="j":
            while True:
                try:
                    indeks=int(input("Mis on järjekorranumber? "))
                    if 1<=indeks<=len(nimed):
                        break
                except ValueError:
                    print("vale andmetüüp")
            nimed.pop(indeks-1)
        elif v=="n":
            nimi=input("Sisesta nimi: ")
            mitu=nimed.count(nimi)
            if mitu>0:
                for i in range(mitu):
                    nimed.remove(nimi)
            else:
                print(f"{nimi} puudub")
    elif v=="S":
        v=int(input("A-z?(1) või Z-a?(2)"))
        if v==1:
            nimed.sort()
        elif v==2:
            nimed.sort(reverse=True)
    elif v=="E":
        nimed.clear()
        print("Andmed on kustutatud")
    elif v=="P":
        print("Oli:",nimed)
        nimed.reverse()
        print("Nüüd:",nimed)
    elif v=="C":
        nimed2=[]
        print("Oli:",nimed2)
        nimed2=nimed.copy()
        print("Nüüd:",nimed2)
    elif v=="I":
        nimi=input("Sisesta nimi: ")
        mitu=nimed.count(nimi)
        if mitu>0:
            indeks=-1
            for i in range(mitu):
                indeks=nimed.index(nimi,indeks+1)
                print(indeks)
        else:
            print(f"{nimi} puubub")













#sõna="Programmeerimine" #str
#print(sõna)
#loetelu=list(sõna)
#n=len(loetelu)
#print(f"Sõnas {sõna} on {n} tähed")
#print(loetelu)
