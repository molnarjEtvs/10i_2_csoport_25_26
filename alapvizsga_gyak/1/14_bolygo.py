import os
os.system("cls")

def bolygoRogzites():
    bolygok = []
    while True:
        bolygo= input("addja meg a bolygo nevét")
        if not bolygo:
            break
        bolygok.append(bolygo.capitalize())
    return bolygok
def bolygoElemzes(bolygok:list):
    bolygokdb = len(bolygok)
    print(f"{bolygokdb} került rögzítésre.")
    darabszam = 0
    for x in bolygok:
        if len(x)==4:
            darabszam += 1 
    print(f"4 betűsek száma:{darabszam}db")
    szoveg = "_$_".join(bolygok)
    print(f"Rögzített bolygók: {szoveg}")                   
b = bolygoRogzites()
bolygoElemzes(b)