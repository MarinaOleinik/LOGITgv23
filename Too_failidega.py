from genericpath import isfile
from os import *
def loe_failist(fail:str)->list:
    """Loetakse informatsioon failist ja tagastatakse info nagu järjend
    :param str fail: faili nimetus
    .rtype: list
    """
    f=open(fail,'r',encoding="utf-8-sig")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):
    """Ümber salvestame järdjendi failisse
    """
    for i in range(7):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'w',encoding="utf-8")
    for element in järjend:
        f.write(element+'\n')
    f.close()
def teksti_lisamine_failisse(fail:list,text:str):
    f=open(fail,'a',encoding="utf-8-sig")
    f.write(text+'\n')
    f.close()

#--------------kasutamine----------------
if path.isfile("Text.txt"): remove("Text.txt") #path.isdir(kaust)



for i in range(4):
    tekst=input("Sisesta mingi tekst faili lisamiseks: ")
    teksti_lisamine_failisse("Text2.txt",tekst)
j=loe_failist("Text2.txt")
for i in j:
    print(i)
with open("Text2.txt",'r') as f:
    print(f.read())


kirjuta_failisse("List.txt")



kuud=loe_failist("Kuud.txt")
print(kuud) #reas
for kuu in kuud:
    print(kuu) #veerus

