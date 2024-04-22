import math

a = [1, 1]
ax = 1
ay = 1

b = [5, 1]
bx = 5
by = 1

c = [5, 4]
cx = 5
cy = 4

x = []
abcx = [ax, bx, cx]
abcy = [ay, by, cy]

def dali_su_iste_tocke(x1, x2, x3):
    if x1 == x2 or x1 == x3 or x2 == x3:
        return True
    else:
        return False

iste_tocke= dali_su_iste_tocke(a, b, c)


def provjera_kuta(lista, rezultat):
    for kordinata in lista:
        if lista.count(kordinata) == 2:
            rezultat += 1
        else:
            rezultat -= 1
    return rezultat

xevi = provjera_kuta(abcx, 0)
print(xevi)
ysiloni = provjera_kuta(abcy, 0)
print(ysiloni)

class ProvjeraKuta:
    def __init__(self, x_lista, y_lista):
        self.xevi = self.pk(x_lista, 0)
        self.ysiloni = self.pk(y_lista, 0)
        self.good_to_go = False
        self.dali_su_ok()

    def pk(self, lista, rezultat):
        for kordinata in lista:
            if lista.count(kordinata) == 2:
                rezultat += 1
            else:
                rezultat -= 1
        return rezultat

    def dali_su_ok(self):
        if self.xevi == 1 and self.ysiloni == 1:
            self.good_to_go = True
            # return self.good_to_go

kutevi = ProvjeraKuta(abcx, abcy)
print(kutevi.good_to_go)

def udaljenost(tocka1, tocka2):
    return math.sqrt((tocka2[0] - tocka1[0])**2 + (tocka2[1] - tocka1[1])**2)

def dijagonala_pravokutnika(tocka1, tocka2, tocka3):
    duljina_stranice1 = udaljenost(tocka1, tocka2)
    duljina_stranice2 = udaljenost(tocka1, tocka3)
    duljina_stranice3 = udaljenost(tocka2, tocka3)
    return math.sqrt(duljina_stranice1**2 + duljina_stranice2**2) if duljina_stranice1 == duljina_stranice3 else math.sqrt(duljina_stranice1**2 + duljina_stranice3**2)

dijagonala = dijagonala_pravokutnika(a, b, c)

print(dijagonala)




# 1 Točke moraju biti međusobno različite.
# 2 Pravokutnik mora biti pravilno orijentiran u ravnini, tj. točke moraju biti poredane tako da se stvore suprotni kutovi.
# 3 Dijagonale pravokutnika se sijeku točno na sredini.
# od 3 taočke moraju imati 2x isti x i 2x isti y

