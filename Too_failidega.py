from os import remove, path,system
from gtts import *

def loe_failist(fail:str)->list:
    """Loetakse informatsioon failist ja tagastatakse info nagu järjend
    :param str fail: faili nimetus
    .rtype: list
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend

def kirjuta_failisse(fail:str,järjend=[]):
    """Ümber salvestame järdjendi failisse
    """
    for i in range(3):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'w',encoding="utf-8")
    for element in järjend:
        f.write(element+'\n')
    f.close()

def teksti_lisamine_failisse(fail:list,text:str):
    f=open(fail,'a')
    f.write(text+'\n')
    f.close()

def faili_kustutamine():
    faili_nimi=input("Mis fail on vaja kustutada ära?")
    if path.isfile(faili_nimi): 
        remove(faili_nimi) #path.isdir(kaust)
        print(f"Fail {faili_nimi} oli kustutatud")
    else:
        print(f"Fail {faili_nimi} puudub")

def räägimine(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")
#--------------kasutamine----------------
#kirjuta_failisse("Kuud.txt")
list_=loe_failist("Kuud.txt")
text=""
for el in list_:
    text+=el+" "
räägimine(text,"et") #terve tekst

for sona in list_: #ühe sõna kaupa
    räägimine(sona,"et")


#faili_kustutamine()

#for i in range(4):
#    tekst=input("Sisesta mingi tekst faili lisamiseks: ")
#    teksti_lisamine_failisse("Text2.txt",tekst)
#j=loe_failist("Text2.txt")
#for i in j:
#    print(i)
#with open("Text2.txt",'r') as f:
#    print(f.read())


#kirjuta_failisse("List.txt")



#kuud=loe_failist("Kuud.txt")
#print(kuud) #reas
#for kuu in kuud:
#    print(kuu) #veerus

