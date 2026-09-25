class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumaara}')


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')
        print(f'Päätoimittaja: {self.paatoimittaja}')



lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

lehti.tulosta_tiedot()
print()
kirja.tulosta_tiedot()

#tehtävä2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = nopeus

    def aja(self, tuntimaara):
        self.matkamittari += self.nopeus * tuntimaara


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko



sahkoauto = Sahkoauto('ABC-15', 180, 52.5)
polttomoottoriauto = Polttomoottoriauto('ACD-123', 165, 32.3)

sahkoauto.aseta_nopeus(120)
polttomoottoriauto.aseta_nopeus(100)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print(f'Sähköauton matkamittari: {sahkoauto.matkamittari} km')
print(f'Polttomoottoriauton matkamittari: {polttomoottoriauto.matkamittari} km')
