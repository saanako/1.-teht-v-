

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä



auto = Auto('ABC-123', 142)

print('Rekisteritunnus:', auto.rekisteritunnus)
print('Huippunopeus:', auto.huippunopeus)
print('Nopeus:', auto.nopeus)
print('Kuljettu matka:', auto.kuljettu_matka)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print('Nopeus kiihdytysten jälkeen:', auto.nopeus)

auto.kiihdytä(-200)

print('Nopeus hätäjarrutuksen jälkeen:', auto.nopeus)



 






