import math

import kordinate
from kordinate import *

x_kordinate_od_abc = [ax, bx, cx]
y_kordinate_od_abc = [ay, by, cy]
x_od_abcd = x_kordinate_od_abc
y_od_abcd = y_kordinate_od_abc

def kordinate_D(a, b, c):
    # global D
    # D = []
    x_od_D = c[0] - b[0] + a[0]
    y_od_D = c[1] - b[1] + a[1]
#     D.append(x_od_D, y_od_D)
    D[0] = x_od_D
    D[1] = y_od_D
    x_od_abcd.append(x_od_D)
    y_od_abcd.append(y_od_D)
    # kordinate.D = [x_od_D, y_od_D]
    # # return kordinate.D
    # dx = x_od_D
    # dy = y_od_D
    # D = [dx, dy]

def dali_su_tocke_razlicite(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


class ProvjeraKuteva:
    def __init__(self, x_lista, y_lista):
        self.sve_x_kordinate = self.provjera_kuta(x_lista, 0)
        self.sve_y_kordinate = self.provjera_kuta(y_lista, 0)
        self.kutevi_su_ok = False

    def provjera_kuta(self, lista, rezultat):
        for kordinata in lista:
            if lista.count(kordinata) == 2:
                rezultat += 1
            else:
                rezultat -= 1
        return rezultat

    def dali_su_kutevi_ok(self):
        if self.sve_x_kordinate == 1 and self.sve_y_kordinate == 1:
            self.kutevi_su_ok = True



def dali_je_X_unutar_pravokutnika():
    if xx < max(x_od_abcd) and xy < max(y_od_abcd):
        return True
    else:
        return False

# def izracun_tocke_D(a, b, c):
#     global D
#     x_od_D = c[0] - b[0] + a[0]
#     y_od_D = c[1] - b[1] + a[1]
#     x_od_abcd.append(x_od_D)
#     y_od_abcd.append(y_od_D)
#     D = [x_od_D, y_od_D]


def dijagonala_izracun(a, b, c, d):
    def udaljenost(tocka1, tocka2):
        return math.sqrt((tocka2[0] - tocka1[0]) ** 2 + (tocka2[1] - tocka1[1]) ** 2)
    duljina_stranice1 = udaljenost(a, b)
    duljina_stranice2 = udaljenost(b, c)
    duljina_stranice3 = udaljenost(c, d)
    duljina_stranice4 = udaljenost(d, a)
    if duljina_stranice1 == duljina_stranice2 and duljina_stranice1 == duljina_stranice3 and \
        duljina_stranice2 == duljina_stranice3 and duljina_stranice4 == duljina_stranice1:
        diagonala = duljina_stranice1 * math.sqrt(2)
        return f"Dijagonala kvadrata je {diagonala}"
    else:
        diagonala = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        return f"Dijagonala pravokutnika je {diagonala}"


# def izracun_tocke_D(a, b, c):
#     global D
#     x_od_D = c[0] - b[0] + a[0]
#     y_od_D = c[1] - b[1] + a[1]
#     x_od_abcd.append(x_od_D)
#     y_od_abcd.append(y_od_D)
#     D = [x_od_D, y_od_D]


