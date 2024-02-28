#from Mymodul import *
#b=int(input("Sisesta arv2: "))
#summa_3=Summa(3,b,int(input("kolmas arv: ")))
#summa_31=Summa(100,100)
#print(summa_3)
#print(summa_31)
#2
#from Mymodul import *
#try:
#    aasta=float(input("Sisestage Aasta: "))
#    print(liigaasta(aasta))
#except ValueError:
#    pass

#3
#from Mymodul import *
#try:
#    ruudukülg = int(input("Palun sisestage ruudu küljed: "))
#    if ruudukülg != ruudukülg:
#        print("Palun sisestage 3 küljet.")
#    else:
#        perimeeter, pindala, diagonaal = square(ruudukülg)
#        print(perimeeter, pindala, round(diagonaal, 2))
#except ValueError:
#    print("Palun sisestage kehtiv külje pikkus numbrina.")


#4
#from Mymodul import *
#while True:
#    try:
#        kuu=int(input("kuu number: "))
#        break
#    except:
#        print("viga")
#a=season(kuu)
#print(a)


#6

#from Mymodul import *
#arv=int(input("Sisestage arvu: "))
#print(is_prime(arv))


#7

#from Mymodul import *
#paev=int(input("kirjutage paeva: "))
#kuu=int(input("kirjutage kuut: "))
#aasta=int(input("kirjutage aasta: "))

#print(date(paev, kuu, aasta))

#from Mymodul import *
#a=float(input("sisestage a raha: "))
#aasta=int(input("Sisestage kui palju aastaks: "))

#print("teie tagastatud summa on: ",pank(a,aasta))

def Palgad_Inimesed(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus inmesi ja plaka
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    :param list n: Inimeste arv
    :rtype list, list

    """
    if n>0:
        for j in range(n):
            nimi=input("Sisestage nimi: ").capitalize()
            palk=int(input("Sisestage palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p  
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    for j in range(len(i)):
        print(i[j],"-",p[j])

def andmete_emaaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andid ja tagastab listitud järjendid
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    nimi=input("Keda kustutada ära(nimi): ")

    for j in range(0,len(i)):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p

def kellel_on_suurim_palk(i:list,p:list)->list:
    """Funktsioon näitab kellel on suurim palk
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    nimed=[]
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def kellel_on_vahem_palk(i:list,p:list)->list:
    """Funktsioon näitab kellel on väiksem palk
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    nimed=[]
    min_palk=min(p)
    ind=-1
    for palk in p:
        if palk==min_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed


def sorteerimine(i:list,p:list):
    """Funktsiooni teeb palgade sorteerimist 

    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    for n in range(0, len(i)):
        for n in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]

    return i,p
