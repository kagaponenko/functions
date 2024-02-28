# from MyModul import *
# # #1
# # summa_3=Summa(5,8,12)
# # print(summa_3)
# # #2
# # a=float(input("Arv1: "))
# # b=float(input("Arv2: "))
# # summa_3=Summa(a,b)
# # print(summa_3)
# # #3
# # summa_3=Summa(
# #     float(input("Arv1: ")),
# #     float(input("Arv2: ")),
# #     float(input("Arv3: ")))
# # print(summa_3)


# #(1)
# a=int(input("Arv1: "))
# t=input("Tehe: ")
# b=int(input("Arv2: "))
# vastus=arithmetic(a,b,t)
# print(f"{a}{t}{b}=",vastus,sep="")

# #(2)
# from random import *
# for i in range(5):
#     aasta=randint(1900,2200)
#     if is_year_leap(aasta):
#         print(f"Aasta {aasta} on liigaasta")
#     else:
#         print(f"Aasta {aasta} on tavaline")

# #(3)
# a=float(input("Riidukulg: "))
# S,P,D=square(a)
# print("S=",S)
# print("P=",P)
# print("D=",D)

# #(4)
# nr=int(input("Kuu jarjakorranumber: "))
# vastus=season(nr)
# print(vastus)

# #(5)
# summa=float(input("Summa: "))
# aastad=int(input("Aastad: "))
# summa=bank(summa,aastad)
# print(f"{aastad} aasta parast summa on {summa}")

# #(6)
# v=int(input("Sisesta arv: "))
# if is_prime(v):
#     print("Tavaline arv")
# else:
#     print("Liitarv")
    
# #(7)
# p=25
# k=12
# a=2025
# t=date_(p,k,a)
# print(t)


    ####    ####

from PalgadeModul import *

palgad=[1200,2500,750,395,1200,2500]
inimesed=["A","B","C","D","E","D"]

while True:
    print("0-Andmed ekraanile\n1-Andmete lisamine\n2-Andmete emaldamine\n3-Kellele on surim palk\n4-Sorterimine\n")
    vastus=int(input())
    if vastus==0:
        naita_andmed(inimesed,palgad)
    elif vastus==1:
        inimesed,palgad=andmete_lisamine(inimesed,palgad)
    elif vastus==2:
        inimesed,palgad=andmete_kustutamine(inimesed,palgad)
    elif vastus==3:
        rikkad_inimesed=kellel_on_surim_palk(inimesed,palgad)
        print(rikkad_inimesed)
    elif vastus==4:
        inimesed,palgad=sorteerimine(inimesed,palgad)