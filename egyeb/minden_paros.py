import os
os.system("cls")

szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg az második számot: "))
szam3 = int(input("Add meg az harmadik számot: "))

if szam1%2 == 0 and szam2%2==0 and szam3%2 == 0:
    print("Mind a három szám páros")
else:
    print("Valamelyik nem páros")