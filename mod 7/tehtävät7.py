#tehtävä 1

#import random

#def noppa():
#    return random.randint (1, 6)

#while True:
#    silmaluku = noppa ()
#    print(silmaluku)
#    if silmaluku == 6:
#        break


#tehtävä 2


#import random

#def noppa(tahkot):
#    return random.randint (1, tahkot)

#maksimi = int(input('Anna nopan tahkojen määrä: '))

#while True:
#    silmaluku = noppa(maksimi)
#    print(silmaluku)
#    if silmaluku == maksimi:
#        break

#tehtävä 3

#1 gallona = 3,785 litraa

#yksikkömuunnos = litrat = gallonat * 3,785

#def gallonat (gallona):
#    return gallona * 3,785

#litrat = gallonat ()

#gallonat = float(input('anna gallona määrä: '))
#while gallonat >= 0:
#    ...

#tehtävä 4

#lista1 = [1, 6, 8, 9,]

#def luvut (lista1):
#    return sum (lista1)

#tulos = luvut(lista1)
#print(f'lukujen summa on {tulos}')


#tehtävä 5

def karsi_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista


luvut = [1, 2, 3, 4, 5, 6, 7, 8]

karsittu = karsi_parittomat(luvut)

print('Alkuperäinen lista:', luvut)
print('Karsittu lista:', karsittu)


