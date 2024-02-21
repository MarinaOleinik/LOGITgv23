from math import *
from datetime import datetime
def date_(paev:int,kuu:int,aasta:int)->bool:
    """
    """
    try:
        d=datetime(aasta,kuu,paev)
        print(d)
        tulemus=True
    except:
        tulemus=False
    return tulemus


def is_prime(num:int)->bool:
    """
    """
    p=True
    if num>=0 and num<1001:
        for i in range(2,num):
            if num%i==0:
                p=False
    return p


def bank(a:float,years:int)->float:
    """
    """
    for i in range(years):
        a=a*1.1
    return a

def season(number:int)->str:
    """
    """
    if number>0 and number<13:
        if number in [1,2,12]:
            s="talv"
        elif number in [3,4,5]:
            s="kevad"
        elif number in [6,7,8]:
            s="suvi"
        else:
            s="sügis"
    else:
        s="vale number"
    return s


def square(külg:float)->any:
    """Leiab: pindala-S,ümbermõõt-P,diagonaal-D

    :param float külg:
    :rtype: any
    """
    S=külg**2
    P=4*külg
    D=sqrt(2*külg**2)
    return S,P,D

def is_year_leap(aasta:int)->bool:
    """Tagastab True kui aasta on liigaaasta ja False, kui on tavaline aasta
    :param int aasta: Kasutaja sisestab aasta jarjekorranumber
    :rtype: bool
    """
    if aasta%4==0:
        tüüp=True
    else:
        tüüp=False
    return tüüp

def arithmetic(a:int,t:str,b:int)->any:
    """Funktsioon tagastab kas +,-,*,/ tehede tulemust.
        + -liitmine,
        - -lahutamine,
        * -korrutamine,
        / -jagamine
    :param int a: Esimene arv
    :param int b: Teine arv
    :param str t: Tehe
    :rtype: any
    """
    if t in ["+","-","/","*"]:
        if t=="+":
            v=a+b
        elif t=="-":
            v=a-b
        elif t=="*":
            v=a*b
        else:
            if b==0:
                v="DIV/0"
            else:
                v=a/b
    else:
        v="Tundmatu tehe"
    return v

def Summa(arv1:float,arv2:float,arv3=5.0)->float:
    """Funktsioon tagastab kolme arvude summa float formaadis. Kolmas arv vaikimisi võrdub 5.0.
    :param float arv1: Esimene arv, mis sisestab kasutaja
    :param float arv2: Teine arv, mis sisestab kasutaja
    :param float arv3: Kolmas arv, mis sisestab kasutaja või väikimisi =5.0
    :rtype: float
    """
    s=arv1+arv2+arv3
    return s