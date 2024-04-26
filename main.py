from formule import *

# AKO SU KORDINATE 2D:
if len(a) < 3:
    iste_kordinate_tocaka = dali_su_tocke_razlicite(a, b, c)
    if iste_kordinate_tocaka == True:
        print("Molim Vas unesite različite kordinate")
    else:
        pravokutnik = ProvjeraKuteva(x_kordinate_od_abc, y_kordinate_od_abc)
        pravokutnik.dali_su_kutevi_ok()
        if pravokutnik.kutevi_su_ok == False:
            print("Kordinate ne tvore pravokutnik")
        else:
            kordinate_D(a, b, c)
    print(f"""{ax}, {ay}
{bx}, {by}
{cx}, {cy}
{d[0]}, {d[1]}
X unutar kvadra: {dali_je_X_unutar_pravokutnika()}
            """)
    print(dijagonala_izracun(a, b, c, d))

# AKO SU KORDINATE 3D
else:
    print(f"""{a[0]}, {a[1]}, {a[2]}
{b[0]}, {b[1]}, {b[2]}
{c[0]}, {c[1]}, {c[2]}
{d[0]}, {d[1]}, {d[2]}
{x[0]}, {x[1]}, {x[2]}
Prostorna dijagonala je {prostorna_dijagonala_kvadra(a, b, c, d)}
X unitar kvadra: {provjeri_kvadra(a, a, c, d, x)}""")












