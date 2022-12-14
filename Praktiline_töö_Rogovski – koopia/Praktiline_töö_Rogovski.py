from math import *
from tkinter import FALSE
from unicodedata import *

print("puu läbimõõdu")
try:
    c = float (input("Anna ümbermõõd:"))
    if c>0:
        d = round (c/pi, 2)
        print(f"Puu läbimõõd on: = {d}")
    else:
        print("C peab olema suurem kui 0")
except:
    print("Vali andmetüüp")



print ("maatüki diagonaal")

N = (input("Anna N:"))
M = (input("Anna M:"))
if  N.isalpha() == True and M.isalpha() == True:
    print("Vali andmetüüp") 
elif N>0 and M>0:
    print("Peab olema suurem kui 0")
else:
    C = round(sqrt(N**2+M**2), 2)
    print (f"ristkülikukujulise maatüki diagonaal: = {C}")


try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    if aeg>0 and teepikkus>0:
        kiirus = teepikkus / aeg
        print("Sinu kiirus oli " + str(kiirus) + " km/h")
    else:
        print("Peab olema suurem kui 0")
except:
    print("vali andmetüüp")


print ("aritmeetilise keskmise")
try:
    num1 = int(input("Anna arv number üks:"))
    num2 = int(input("Anna arv number kaks:"))
    num3 = int(input("Anna arv number kolm:"))
    num4 = int(input("Anna arv number neli:"))
    num5 = int(input("Anna arv number viis:"))
    if num1>0 and num2>0 and num3>0 and num4>0 and num5>0:
        total = (num1+num2+num3+num4+num5)/5
        print (f"aritmeetilise keskmise on: = {total}")
    else:
        print("Peab olema suurem kui 0")
except:
    print("Vali andmetüüp")

print ("Konn")
print ('   @..@\n  (----)\n ( \__/ )\n ^^ "" ^^')

print("kolmnurga ümbermõõdu")
try:
    ak = int(input("Anna a:"))
    bk = int(input("Anna b:"))
    ck = int(input("Anna c:"))
    if ak>0 and bk>0 and ck>0:
        Umbermood = ak+bk+ck
        print (f"Kolmnurga ümbermõõd on: = {Umbermood}")
    else:
        print("Peab olema suurem kui 0")
except:
    print("Vali andmetüüp")

print("pitsa")
try:
    P = int(input("Kui palju sõbrad?"))
    if P>0:
        Summa = round((12.90*1.1)/P, 2)
        print (f"Iga sõbra peab maksma: = {Summa}")
    else:
        print("Peab olema suurem kui 0")
except:
    print ("Vali andmetüüp")


print("Kütusekulu arvutamine")
try:
    liiter = float(input("kütuse liitrid:"))
    kilomeetr = float(input("läbitud kilomeetrid:"))
    if liiter>0 and kilomeetr>0:
        kütusekulu = liiter/kilomeetr*100
        print(f" kütusekulu 100km kohta keskmiselt: = {kütusekulu}")
    else:
        print("Peab olema suurem kui 0")
except:
    print("Vale andmetüüp")


print("Rulluisutajad")
try:
    minut = float(input("Kui palju minutit?"))
    if minut>0:
        S = 29.9*minut
        print (f"Meetrid käinud: = {S}")
    else:
        print("Peab olema suurem kui 0")
except:
    print("Vali andmetüüp")

print("Ajateisendus")
try:
    minutit = int(input("Sisesta aja minutites"))
    if minutit>0:
        H=minutit//60 #hour
        minutit = minutit%60 #min
        print(f"{H}:{minutit}")
    else:
        print("Peab olema suurem kui 0")
except:
    print ("vali andmetüüp")