import os
os.system("cls")

def vizsgaAllapot(pontszam:int):
    if pontszam>=48:
        return True
    else:
        return False
    
while True:
    nev = input("Add meg a vizsgázó nevét: ")
    if not nev:
        break
    pontszam = int(input("Add meg a pontszámot: "))
    if vizsgaAllapot(pontszam) == True:
        print(f"{nev} sikeres vizsgát tett!")
    else:
        print(f"{nev} SIKERTELEN vizsgát tett!")


def hello(nev):
    return "hello"
    print(nev)