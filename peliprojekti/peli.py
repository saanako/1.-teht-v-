nimi = input('kerro minulle nimesi: \n')
ikä = int(input('kerro minulle ikäsi: \n'))

if (ikä < 12):
    print('olet alaikäinen!')
    exit()
if (ikä > 80):
    print('Onko vanhainkodisa tarpeeksi hyvä netti pelaamista varten?!')
if (ikä == 12):
    print(f'onneksi olkoon {nimi} , olet tarpeeksi vanha peliä varten')
else : 
    print (f'hei {nimi} !')

Aseet = []
Asusteet = []
Lemmikit= []

def anna_ase():
   aseesi = input("Alueilla voi olla vaaroja. Ota mukaan ase puolustaaksesi kissojasi. " \
   "mitä aseita haluat käyttää?: \n ")
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
   print("Olet nyt valmis matkaan!")

tulosta_reppu()




class Kissa :
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f'{self.nimi} ({self.paino} kg)'



class Alue:
    def __init__(self, nimi, kissa=None):
        self.nimi = nimi
        self.kissa = kissa


class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.kissat = []
        self.sijainti = sijainti

    

    def hyppää(self, alue):
        self.sijainti = alue
        print(f'Hyppäsit alueelle {alue.nimi}.')

    def nappaa_kissa (self):
        if self.sijainti.kissa is not None:
            kissa = self.sijainti.kissa
            self.kissat.append(kissa)
            self.sijainti.kissa = None
            print(f'Nappasit kissan: {kissa.nimi}')
        else:
            print('Tällä alueella ei näy kissoja, koita etsiä muualta.')

    def pelaaja_profiili(self):
        print(f'Pelaaja: {self.nimi}')
        print(f'Sijainti: {self.sijainti.nimi}')

    
        
        print('Kissat:')
        if len(self.kissat) == 0:
            print('Ei yhtään kissaa.')
        else:
            for Kissa in self.kissat:
                print(f'{Kissa}😺')




kissa1 = Kissa ('Kilpikonnakuvio' , 3.0)
kissa2 = Kissa('Musta pitkäkarva' , 7.0)
kissa3 = Kissa ('Oranssi tabby', 2.0)
kissa4 = Kissa ('Valkoinen lyhytkarva', 4.0)
kissa5 = Kissa ('Venäjän sininen', 5.0)



Alue1 = Alue('Niitty', kissa3 )
Alue2 = Alue('Syysmetsä', kissa1)
Alue3 = Alue('Laakso', kissa4)
Alue4 = Alue('Merenranta', kissa5)
Alue5 = Alue('Vuoristo', kissa2)



pelaaja = Pelaaja('pelaaja', Alue1)



while True:
    print('\n MINNE MENEMME?😺')
    print('1. Mene Niitylle')
    print('2. Mene Syysmetsään')
    print('3. Mene Laaksoon')
    print('4. Mene Merelle')
    print('5. Mene Vuoristoon')
    print('6. Kerää kissa')
    print('7. Näytä pelaajan profiili')
    print('0. Lopeta')

    valinta = input('Valitse toiminto: ')

    if valinta == '1':
        pelaaja.hyppää(Alue1)
    elif valinta == '2':
        pelaaja.hyppää(Alue2)
    elif valinta == '3':
        pelaaja.hyppää(Alue3)
    elif valinta == '4':
        pelaaja.hyppää(Alue4)
    elif valinta == '5':
        pelaaja.hyppää(Alue5)
    elif valinta == '6':
        pelaaja.nappaa_kissa()
    elif valinta == '7':
        pelaaja.pelaaja_profiili()
    elif valinta == '0':
        print('Peli on päättynyt.')
        break
    else:
        print('Ei löydy')

