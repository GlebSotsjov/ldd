#from string import *
##1
#vokaalid = ['a', 'e', 'i', 'o', 'u', '�', '�', '�', '�']
#konsonandid = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', '�', 'z', '�', 't', 'v', 'w', 'x', 'y']
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta s�na v�i lause: ").lower()
#tekst_list=list(tekst)
#for taht in tekst_list:
#    if taht in vokaalid:
#        v+=1
#    elif taht in konsonandid:
#        k+=1
#    elif taht in markid:
#        m+=1
#    else:
#        t+=1
#print("Vokaalid:", v)
#print("konsonandid:", k)
#print("kirjav�hem�rgid:", m)
#print("T�hikud:", t)


names = [input("Sisestage nimi: ") for _ in range(5)]
print("Nimed t�hestikulises j�rjekorras:", sorted(names))

print("Viimati lisatud nimi:", names[-1])

index = int(input("Sisestage nime indeks, mida soovite muuta: "))
new_name = input("Sisestage uus nimi: ")
names[index] = new_name

students = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']

unique_students = list(set(students))
print("Unikaalsed nimed:", unique_students)

ages = [20, 25, 30, 35, 40]

max_age = max(ages)
min_age = min(ages)
total_age = sum(ages)
average_age = total_age / len(ages)

print("Suurim vanus:", max_age)
print("V�ikseim vanus:", min_age)
print("Vanuste kogusumma:", total_age)
print("Keskmine vanus:", average_age)




