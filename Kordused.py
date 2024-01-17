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
