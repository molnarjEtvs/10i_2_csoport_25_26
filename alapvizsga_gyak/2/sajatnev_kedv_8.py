import os
os.system("cls")

try:
    eredeti_ar = int(input("Add meg az eredeti arat:"))
    termek_db = int(input("Adja meg hány terméket vásárolt!: "))
    kedvezmeny_szazalek = float(input("Add meg hány százalék    kedvezmény van a termékre:"))

    kedvezmenyes_ar=eredeti_ar-(eredeti_ar*(kedvezmeny_szazalek/100))
    kedvezmenyes_ar = round(kedvezmenyes_ar,2)
    kedv_osszar=kedvezmenyes_ar*termek_db
    eredeti_osszar=eredeti_ar*termek_db
    if kedv_osszar > 20000:
        kedv_osszar = 20000


except ValueError:
    print("Rossz értéket adtál meg, próbáld újra!")


