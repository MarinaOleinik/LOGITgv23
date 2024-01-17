print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Nimi: ")
print(nimi, ", oi kui ilus nimi!" )
v=int(input(nimi,  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
# input()->"0" or "1", int(input())- 0 or 1
if v==1: #if v=="1"
    print("Indexi leidmine")
    while True:
        try:
            pikkus=int(input("Pikkus: "))
            mass=float(input("Kaal: "))
            break
        except :
            print("Viga!")
    index=mass/(0.01*pikkus)**2
    if index<16:
        print("")
    elif index<19:
        print("")

else:
    print("Kahju! See on väga kasulik info!")