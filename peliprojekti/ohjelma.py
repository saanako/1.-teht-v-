
#1

nimi = input('kerro minulle nimesi: \n')
ika = int(input('kerro minulle ikäsi: \n'))

#2

if (ika < 12):
    print('olet alaikäinen!')
    exit()
if (ika > 80):
    print('Onko vanhainkodisa tarpeeksi hyvä netti pelaamista varten?!')
if (ika == 12):
    print('onneksi olkoon nimi , olet tarpeeksi vanha peliä varten')
else : 
    print (f'hei {nimi} !')


#3


Aseet = []
Asusteet = []
Lemmikit= []

def anna_ase():
   aseesi = input("mitä aseita haluat käyttää?: \n ")
   Aseet.append(aseesi)
   print(f"{aseesi} lisättiin reppuusi!")

anna_ase()

def anna_asuste():
   asusteesi = input("minkä asusteen haluat valita?: \n ")
   Asusteet.append(asusteesi)
   print(f"puit {asusteesi} yllesi!")

anna_asuste()

def anna_lemmikki():
   Lemmikkisi = input("Minkä lemmikin haluat adoptoida?: \n")
   Lemmikit.append(Lemmikkisi)
   print(f"otit {Lemmikkisi} mukaan!")

anna_lemmikki()

def tulosta_reppu():
   print(" \n -- REPUN SISÄLTÖ --")
   print(f"Aseet:{Aseet} ")
   print(f"Asusteet:{Asusteet}")
   print(f"lemmikit:{Lemmikit}")

tulosta_reppu()


   




   
   
   

