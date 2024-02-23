def Summa(arv1:float,arv2:float,arv3=5.0)->float:
    """Funktsioon tagastab kolme arvude summa float formaadis. Kolmas arv vaikimisi vordub 5.0.
    :param float arv1: Esimene arv,mis sisestab kasutaja
    :param float arv2: Teine arv,mis sisestab kasutaja
    :param float arv3: Kolmas arv,mis sisestab kasutaja voi vaikimisi = 5.0
    rtype: float
    """
    s=arv1+arv2+arv3
    return s


def arithmetic(a:int,b:int,t:str)->any:
    """Funktsioon tagastab kas +,-,*,/ tehede tilemust.
        + -liitmine,
        - -lahutamine,
        * -korrutamine,
        / -jagamine
    :param int a: Esimine arv
    :param int b: Teinene arv
    :param int t: Kolmas arv
    rtype: any
    """
    if t in ["+","-","*","/"]:
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
    

def is_year_leap(aasta:int)->bool:
    """Tagastab True kui aasta on liigaaasta ja False, kui on tavaline aasta
    :param int aasta: Kasutaja sisestab aasta jarjekorranumber
    rtype: bool
    """
    if aasta%4==0:
        tuup=True
    else:
        tuup=False
    return tuup


from math import *
def square(kulg:float)->any:
    """Leiab: pindala-S,umbermoot-P,diagonaal-D
    :param float kulg:
    :rtype: any
    """
    S=kulg**2
    P=4*kulg
    D=sqrt(2*kulg**2)
    return S,P,D


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
            s="sugis"
    else:
        s="vale number"
    return s


def bank(a:float,years:int)->float:
    """
    
    """
    for i in range(years):
        a*=1.1
    return a


def is_prime(num:int)->bool:
    """
    
    """
    p=True
    if num>=0 and num<1001:
        for i in range(2,num):
            if num%i==0:
                p=False
    return p


from datetime import *
def date_(paev:int,kuu:int,aasta:int)->bool:
    """
    
    """
    try:
        d=datetime(aasta,kuu,paev)
        tulemus=True
    except:
        tulemus=False
    return tulemus