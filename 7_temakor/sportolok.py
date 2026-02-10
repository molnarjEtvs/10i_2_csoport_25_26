import os,random
os.system("cls")

sportolok = []
while True:
    nev = input("Add meg a nevet: ")
    if nev.lower() == "vége":
        break
    rajtszam = int(input("Add meg a rajtszámot: "))
    atlagseb = random.uniform(8,18)
    sportolo = {}
    sportolo['nev'] = nev
    sportolo['rajtszam'] = rajtszam
    sportolo['atlagseb'] = atlagseb
    sportolok.append(sportolo)

print(sportolok)