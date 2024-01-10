from math import * 
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu ümbermõõt", round(P,1))
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print('Ristküliku pindala', S)# koment
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => '))
d=2*r
print("Ringi läbimõõt", d)
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))
