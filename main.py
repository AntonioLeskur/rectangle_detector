import math

A = [1, 1]
ax = A[0]
ay = A[1]

B = [5, 1]
bx = B[0]
by = B[1]

C = [5, 4]
cx = C[0]
cy = C[1]

X = [13, 13]
xx = X[0]
xy = X[1]


abcx = [ax, bx, cx]
abcy = [ay, by, cy]
abcdx = abcx
abcdy = abcy

def dali_su_iste_tocke(x1, x2, x3):
    if x1 == x2 or x1 == x3 or x2 == x3:
        return True
    else:
        return False

iste_tocke= dali_su_iste_tocke(A, B, C)


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



def izracun_tocke_D(a, b, c):
    D = [0, 0]
    D[0] = c[0] - b[0] + a[0]
    D[1] = c[1] - b[1] + a[1]
    abcdx.append(D[0])
    abcdy.append(D[1])
    return D

print(izracun_tocke_D(A, B, C))


print(abcdx, abcdy)

def is_x_inside():
    if xx < max(abcx) and xy < max(abcy):
        print("X is inside!")
    else:
        print("X is not inside")

is_x_inside()


# DIJAGONALA PRAVOKUTNIKA I DIJAGONALA SE NE IZRAČUNAVAJU JEDNAKO
# PROVJERI FORMULOM DALI JE JEDNO IILI DRUGO (PO DULJINAMA STRANICA)
# I NA TEMELJU TOKA ODABERI FORMULU ZA IZRAČUN !!!!!!!!!!
#
# def calculate_rectangle_diagonal(a, b):
#     # Dijagonala pravokutnika
#     diagonal = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
#     return diagonal
#
# def calculate_square_diagonal(a):
#     # Dijagonala kvadrata
#     diagonal = a * math.sqrt(2)
#     return diagonal

def dijagonala_pravokutnika(tocka1, tocka2, tocka3):
    duljina_stranice1 = udaljenost(tocka1, tocka2)
    duljina_stranice2 = udaljenost(tocka1, tocka3)
    duljina_stranice3 = udaljenost(tocka2, tocka3)
    return math.sqrt(duljina_stranice1**2 + duljina_stranice2**2) if duljina_stranice1 == duljina_stranice3 \
        else math.sqrt(duljina_stranice1**2 + duljina_stranice3**2)

dijagonala = dijagonala_pravokutnika(A, B, C)
print(dijagonala)
