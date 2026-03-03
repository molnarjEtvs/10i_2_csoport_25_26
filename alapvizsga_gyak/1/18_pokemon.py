import os, random
os.system("cls")

class Pokemon:
    def __init__(self,dex:int,nev:str,ero:float):
        self.dex = dex
        self.nev = nev
        self.ero = ero
    def beallitas(self):
        self.ugrasm = self.ero*3*0.885
        
    def kepessegValasztas(self):
        kepessegLista = ["párolgás", "tűzhányás", "lövés", "gurulás"]
        self.kepesseg = random.choice(kepessegLista)

    def csoportositas(self,kor:int):
        if kor >= 15:
            self.csoport="idős"
        else:
            self.csoport="fiatal"

    

pokemonok=[]
with open("pokemonLista.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(',')
        pokemon1 = Pokemon(int(adatok[0]),adatok[1],float(adatok[2]))
        pokemon1.beallitas()
        pokemon1.kepessegValasztas()
        pokemon1.csoportositas(random.randint(1,50))
        pokemonok.append(pokemon1)
        del pokemon1
with open("Pokeadatok.txt","w", encoding="utf-8") as szia:
    for poke in pokemonok:
        szia.write(f"DEX: {poke.dex}\n")
        szia.write(f"NEV: {poke.nev}\n")
        szia.write(f"ERO/UGRASSIM: {poke.ero}KP / {poke.ugrasm}m\n")
        szia.write(f"KEPESSEG/CSOPORT: {poke.kepesseg} / {poke.csoport}\n")
        szia.write(f"*********************************\n")