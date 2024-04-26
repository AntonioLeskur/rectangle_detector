import math
from kordinate import *
import numpy

x_kordinate_od_abc = [ax, bx, cx]
y_kordinate_od_abc = [ay, by, cy]
x_od_abcd = x_kordinate_od_abc
y_od_abcd = y_kordinate_od_abc

def kordinate_D(a, b, c):
    x_od_D = c[0] - b[0] + a[0]
    y_od_D = c[1] - b[1] + a[1]
    d[0] = x_od_D
    d[1] = y_od_D
    x_od_abcd.append(x_od_D)
    y_od_abcd.append(y_od_D)

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

def udaljenost(tocka1, tocka2):
        return math.sqrt((tocka2[0] - tocka1[0]) ** 2 + (tocka2[1] - tocka1[1]) ** 2)

def dijagonala_izracun(a, b, c, d):
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

def provjeri_kvadra(a, b, c, d, x):
    a = numpy.array(a)
    b = numpy.array(b)
    c = numpy.array(c)
    d = numpy.array(d)
    x = numpy.array(x)
    AB = b - a
    AC = c - a
    AD = d - a
    AX = x - a
    BX = x - b
    CX = x - c
    DX = x - d
    if numpy.dot(AB, AC) == 0 and numpy.dot(AB, AD) == 0 and numpy.dot(AC, AD) == 0 and \
        (numpy.dot(AB, AX) > 0 and numpy.dot(AB, BX) > 0 and
                numpy.dot(AC, AX) > 0 and numpy.dot(AC, CX) > 0 and
                numpy.dot(AD, AX) > 0 and numpy.dot(AD, DX) > 0):
        return True
    else:
        return False

def prostorna_dijagonala_kvadra(A, B, C, D):
    a = udaljenost(A, B)
    b = udaljenost(A, C)
    c = udaljenost(A, D)

    dijagonala = numpy.sqrt(a**2 + b**2 + c**2)
    return dijagonala
