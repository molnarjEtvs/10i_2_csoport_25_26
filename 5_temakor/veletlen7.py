import os,random
os.system("cls")

fszam = int(input("Adj meg egy szamot 10-1000 között: "))
gszam = random.randint(10,1000)

print(f"Generált: {gszam}, felhasználó: {fszam}")
if gszam>fszam:
    print("A generált szám nagyobb")
elif gszam<fszam:
    print("A felhasználó szám nagyobb")
else:
    print("egyenlő")