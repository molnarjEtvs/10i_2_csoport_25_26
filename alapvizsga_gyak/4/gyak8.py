import os
os.system("cls")

try:
    kor = int(input("Add meg hány éves vagy: "))
    termekAr = int(input("Add meg a termék árát: "))
    if kor>=10 and kor<=14:
        kedvezmeny = 20
    elif kor>=15 and kor<=25:
        kedvezmeny = 17.5
    elif kor>25 and kor<=35:
        kedvezmeny = 15
    else:
        kedvezmeny = 0
    kedvezmenyMerteke = termekAr * (kedvezmeny/100)
    kedvezmenyesAr = termekAr - kedvezmenyMerteke
    print(f"Kedvezmény: {kedvezmenyMerteke} Ft")
    print(f"kedvezmenyes ár: {kedvezmenyesAr} Ft")
    print(f"Kedvezmény(%): {kedvezmeny}%")
except:
    print("Kérlek számokat adj meg")
