import math
from kordinate import *

x_kordinate_od_abc = [ax, bx, cx]
y_kordinate_od_abc = [ay, by, cy]
x_od_abcd = x_kordinate_od_abc
y_od_abcd = y_kordinate_od_abc


def dali_su_tocke_razlicite(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False
class ProvjeraKuteva:
    def __init__(self, x_lista, y_lista):
        self.sve_x_kordinate = self.provjera_kuta(x_lista, 0)
        self.sve_y_kordinate = self.provjera_kuta(y_lista, 0)
        self.kutrvi_su_ok = False
        self.dali_su_kutevi_ok()

    def provjera_kuta(self, lista, rezultat):
        for kordinata in lista:
            if lista.count(kordinata) == 2:
                rezultat += 1
            else:
                rezultat -= 1
        return rezultat

    def dali_su_kutevi_ok(self):
        if self.sve_x_kordinate == 1 and self.sve_y_kordinate == 1:
            self.kutrvi_su_ok = True


# def izracun_tocke_D(a, b, c):
#     D[0] = c[0] - b[0] + a[0]
#     D[1] = c[1] - b[1] + a[1]
#     x_od_abcd.append(D[0])
#     y_od_abcd.append(D[1])
#     return D
def izracun_tocke_D(a, b, c):
    global D
    # D = [0, 0]
    x_od_D = c[0] - b[0] + a[0]
    # print(x_od_D)
    y_od_D = c[1] - b[1] + a[1]
    x_od_abcd.append(D[0])
    y_od_abcd.append(D[1])
    D = [x_od_D, y_od_D]
izracun_tocke_D(A, B, C)

def dali_je_X_unutar_pravokutnika():
    if xx < max(x_od_abcd) and xy < max(y_od_abcd):
        return True
    else:
        return False


def dijagonala_izracun(a, b, c, d):
    def udaljenost(tocka1, tocka2):
        return math.sqrt((tocka2[0] - tocka1[0]) ** 2 + (tocka2[1] - tocka1[1]) ** 2)
    duljina_stranice1 = udaljenost(a, b)
    # print(duljina_stranice1)
    duljina_stranice2 = udaljenost(b, c)
    # print(duljina_stranice2)
    duljina_stranice3 = udaljenost(c, d)
    # print(duljina_stranice3)
    duljina_stranice4 = udaljenost(d, a)
    if duljina_stranice1 == duljina_stranice2 and duljina_stranice1 == duljina_stranice3 and \
        duljina_stranice2 == duljina_stranice3 and duljina_stranice4 == duljina_stranice1:
        diagonala = duljina_stranice1 * math.sqrt(2)
        return f"Dijagonala kvadrata je {diagonala}"
    else:
        diagonala = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        return f"Dijagonala pravokutnika je {diagonala}"




iste_kordinate_tocaka = dali_su_tocke_razlicite(A, B, C)
if iste_kordinate_tocaka == True:
    print("Molim Vas unesite različite kordinate")
else:
    pravokutnik = ProvjeraKuteva(x_kordinate_od_abc, y_kordinate_od_abc)
    pravokutnik.dali_su_kutevi_ok()
    if pravokutnik.kutrvi_su_ok == False:
        print("Kordinate ne tvore pravokutnik")
    else:
        izracun_tocke_D(A, B, C)
        print(f"""{ax}, {ay}
{bx}, {by}
{cx}, {cy}
{dx}, {dy}
{dali_je_X_unutar_pravokutnika()}
        """)
print(dijagonala_izracun(A, B, C, D))