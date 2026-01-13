import os
os.system("cls")

telefonszamok = []
while True:
    nev = input("Adj meg egy nevet: ")
    if nev.upper() == "VÉGE":
        break
    telefonszam = {}
    telefonszam['nev'] = nev
    telefonszam['tel'] = input("Add meg a telefonszámát: ")
    telefonszamok.append(telefonszam)

keresettNev = input("Add meg a keresett nevet: ")
talalat = ""
for egyTelefonszam in telefonszamok:
    if egyTelefonszam['nev'] == keresettNev:
        talalat = egyTelefonszam['tel']

if talalat == "":
    print("NINCS TALÁLAT")
else:
    print(talalat)