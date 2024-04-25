import math
from kordinate import *

x_kordinate_od_abc = [ax, bx, cx]
y_kordinate_od_abc = [ay, by, cy]
x_od_abcd = x_kordinate_od_abc
y_od_abcd = y_kordinate_od_abc




# def provjera_kuta(lista, rezultat):
#     for kordinata in lista:
#         if lista.count(kordinata) == 2:
#             rezultat += 1
#         else:
#             rezultat -= 1
#     return rezultat
#
# xevi = provjera_kuta(x_kordinate_od_abc, 0)
# print(xevi)
# ysiloni = provjera_kuta(y_kordinate_od_abc, 0)
# print(ysiloni)

class Provjera_uvjeta:
    def dali_su_tocke_razlicite(self, a, b, c):
        if a == b or a == c or b == c:
            return True
        else:
            return False
    def provjera_kuta(self, lista, rezultat):
        for kordinata in lista:
            if lista.count(kordinata) == 2:
                rezultat += 1
            else:
                rezultat -= 1
        return rezultat
    def __init__(self, x_lista, y_lista):
        self.xevi = self.provjera_kuta(x_lista, 0)
        self.ysiloni = self.provjera_kuta(y_lista, 0)
        self.good_to_go = False
        self.dali_su_ok()

    def dali_su_ok(self):
        if self.xevi == 1 and self.ysiloni == 1:
            self.good_to_go = True
            # return self.good_to_go

uvjeti = Provjera_uvjeta(x_kordinate_od_abc, y_kordinate_od_abc)
print(uvjeti.good_to_go)



def izracun_tocke_D(a, b, c):
    D = [0, 0]
    D[0] = c[0] - b[0] + a[0]
    D[1] = c[1] - b[1] + a[1]
    x_od_abcd.append(D[0])
    y_od_abcd.append(D[1])
    return D


print(izracun_tocke_D(A, B, C))
# print(x_od_abcd, y_od_abcd)

def is_x_inside():
    if xx < max(x_kordinate_od_abc) and xy < max(y_kordinate_od_abc):
        print("X is inside!")
    else:
        print("X is not inside")

is_x_inside()


# DIJAGONALA PRAVOKUTNIKA I DIJAGONALA SE NE IZRAČUNAVAJU JEDNAKO
# PROVJERI FORMULOM DALI JE JEDNO IILI DRUGO (PO DULJINAMA STRANICA)
# I NA TEMELJU TOKA ODABERI FORMULU ZA IZRAČUN !!!!!!!!!!

def udaljenost(tocka1, tocka2):
    return math.sqrt((tocka2[0] - tocka1[0])**2 + (tocka2[1] - tocka1[1])**2)

def dijagonala_izracun(a, b, c):
    duljina_stranice1 = udaljenost(a, b)
    duljina_stranice2 = udaljenost(a, c)
    duljina_stranice3 = udaljenost(b, c)
    if duljina_stranice1 == duljina_stranice2 and duljina_stranice1 == duljina_stranice3 and \
        duljina_stranice2 == duljina_stranice3:
        diagonala = duljina_stranice1 * math.sqrt(2)
        return diagonala
    else:
        diagonala = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        return diagonala

# def calculate_rectangle_diagonal(a, b):
#     # Dijagonala pravokutnika
#     diagonal = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
#     return diagonal
#
# def calculate_square_diagonal(a):
#     # Dijagonala kvadrata
#     diagonal = a * math.sqrt(2)
#     return diagonal

# def dijagonala_pravokutnika(tocka1, tocka2, tocka3):
#     duljina_stranice1 = udaljenost(tocka1, tocka2)
#     duljina_stranice2 = udaljenost(tocka1, tocka3)
#     duljina_stranice3 = udaljenost(tocka2, tocka3)
#     return math.sqrt(duljina_stranice1**2 + duljina_stranice2**2) if duljina_stranice1 == duljina_stranice3 \
#         else math.sqrt(duljina_stranice1**2 + duljina_stranice3**2)

# TESTOVI!
iste_tocke= uvjeti.dali_su_tocke_razlicite(A, B, C)
print(iste_tocke)
dijagonala = dijagonala_izracun(A, B, C)
print(dijagonala)

