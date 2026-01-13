import os,random
os.system("cls")

szamok = []
db = int(input("Hány darabot szeretnél: "))
kezdoErtek = int(input("Add meg a kezdő: "))
vegErtek = int(input("Add meg a véget: "))

for _ in range(db):
    vszam = random.randint(kezdoErtek,vegErtek)
    szamok.append(vszam)

print(szamok)