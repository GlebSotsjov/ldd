from string import *
from venv import create
#1
vokaalid = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'õ']
konsonandid = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
markid=punctuation
v=k=m=t=0
tekst=input("Sisesta sõna või lause: ").lower()
tekst_list=list(tekst)
for taht in tekst_list:
    if taht in vokaalid:
        v+=1
    elif taht in konsonandid:
        k+=1
    elif taht in markid:
        m+=1
    else:
        t+=1
print("Vokaalid:", v)
print("konsonandid:", k)
print("kirjavähemärgid:", m)
print("Tühikud:", t)

2
nimed=[]
for i in range(5):
    nimi=input("Sisestage nimi: ").capitalize()
    nimed.append(nimi)

print("Loetelu oli: ", nimed)
nimed.sort()
print("Loetelu sorteeritud: ", nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep=" ")

print("Viimasena oli lisatud: ", nimed[-1])

nimekogum = []
for i in range(5):
    nimi = input("Sisestage nimi: ").capitalize()
    nimekogum.append(nimi)

nimekogum.sort()
print("Nimed tähestikulises järjekorras:", nimekogum)
viimane_lisatud = nimekogum[-1]
print("Viimati lisatud nimi:", viimane_lisatud)

opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
unikaalsed_opilased = []

for nimi in opilased:
    if nimi not in unikaalsed_opilased:
        unikaalsed_opilased.append(nimi)

print("Unikaalsed nimed:", unikaalsed_opilased)

vanused = [25, 30, 35, 40, 45]
min_vanus = min(vanused)
max_vanus = max(vanused)
summa = sum(vanused)
keskmine = summa / len(vanused)

print("Vähim vanus:", min_vanus)
print("Suurim vanus:", max_vanus)
print("Vanuste kogusumma:", summa)
print("Vanuste keskmine:", keskmine)




nimed=[]
for i in range(5):
    nimi=input("Sisestage nimi: ").capitalize()
    nimed.append(nimi)

print("Loetelu oli: ", nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep=" ")

print("Vimasena oli lisatud: ",nimi)

opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']

nimed = []
for nimi in opilased:
    if nimi not in nimed:
        nimed.append(nimi)

print(nimed)
vanused=[]
for i in range(5):
    vanus=int(input("Sisesta vanus: "))
    vanused.append(vanus)
maksimum=max(vanused)
minimum=min(vanused)
summa=sum(vanused)
keskmine=summa/len(vanused)

print(maksimum, "," , minimum, "," , summa, "," , keskmine)
# kuva ekraanile nimi koos vnusega 

for i in range(5):
    print(nimed[i], "on", vanused[i], "aastad vana")

#3
from random import * 
arvud=[]
N=int(input("Mitu rida joonistame?"))
S=input("Sisestage sümbol mida tahate kasutada: ")
for p in range(N):
    arvud.append(randint(1, 100))
#4
for p in range(N):
    print(arvud[p]*S)
postcode = input("Enter the postcode: ")

if not postcode.isdigit() or len(postcode) != 5:
    print("Invalid postcode")
else:
    county_code = int(postcode[0])
    if county_code == 1:
        print("Tallinn")
    elif county_code == 2:
        print("Narva, Narva-Jõesuu")
    elif county_code == 3:
        print("Kohtla-Järve")
    elif county_code == 4:
        print("Ida-Virumaa, Lääne-Virumaa, Jõgevamaa")
    elif county_code == 5:
        print("Tartu linn")
    elif county_code == 6:
        print("Tartumaa, Põlvamaa, Võrumaa, Valgamaa")
    elif county_code == 7:
        print("Viljandimaa, Järvamaa, Harjumaa, Raplamaa")
    elif county_code == 8:
        print("Pärnumaa")
    elif county_code == 9:
        print("Läänemaa, Hiiumaa, Saaremaa")
    else:
        print("Unknown county")

if county_code in [1, 2, 3]:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")

rida=[]
N=randint(2,25)
for i in range(N):
    rida.append(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mitu elemendi vahetame oma vahel "))
if len(rida)//2>kogus:
    for i in range(kogus):
        a=rida[i]
        rida[i]=rida[len(rida)-i-1]
        rida[len(rida)-1-i]=a
print(rida)

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

if numbers:
    max_num = max(numbers)
    useless_number = max_num / len(numbers)
    print(f"The useless number is: {useless_number}")
else:
    print("The list is empty.")