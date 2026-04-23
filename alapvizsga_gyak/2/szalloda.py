import os,random
os.system("cls")

class Szallashely:
    def __init__(self, nev:str,ar:float,helyekSzam:int):
        self.nev = nev
        self.ar = ar
        self.helyekSzam = helyekSzam 
    def helyfrissites(self,db:int):
        self.helyekSzam += db
        if self.helyekSzam >=21:
            self.helyekSzam=21

    def kedvezmenygeneralas(self):
        kedvezmenyek=[5,10,20,30]
        self.kedvezmenySzazalek = random.choice(kedvezmenyek)
        self.kedvezmenyesAr = self.ar*(100-self.kedvezmenySzazalek)/100
        self.kedvezmenyesAr = round(self.kedvezmenyesAr,3)
szallasok = []
with open ("szallasok.txt","r",encoding="Utf-8") as f:
    for sor in f:
        adatok = sor.strip().split("|")
        sallashely1 = Szallashely(adatok[0],float(adatok[1]),int(adatok[2]))
        sallashely1.helyfrissites(random.randint(1,21))
        sallashely1.kedvezmenygeneralas()
        szallasok.append(sallashely1)
        del sallashely1
with open ("akciosszallasok.txt","w", encoding="utf-8") as a:
    for egyszallas in szallasok:
        a.write(f"Szallas neve: {egyszallas.nev}\n")
        a.write(f"Ár/éjszaka/fő: {egyszallas.ar} Ft\n")
        a.write(f"Kedvezmény mértéke: {egyszallas.kedvezmenySzazalek}\n")
        a.write(f"Kedvezményes éjszaka ára: {egyszallas.kedvezmenyesAr} Ft\n")
        a.write(f"Szabad helyek száma: {egyszallas.helyekSzam} db\n")
        a.write(f"#"*20)
        a.write("\n")