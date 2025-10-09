import os
os.system("cls")

jegyek = []

while True:
    jegy = int(input("Adj meg egy jegyet: "))
    if jegy == 0:
        break
    jegyek.append(jegy)

db = len(jegyek)
legrosszabb = min(jegyek)
legjobb = max(jegyek)
atlag = sum(jegyek)/db

print(f"Darabszám: {db}db\nLegjobb:{legjobb}\nLegrosszabb:{legrosszabb}\nÁtlag:{atlag}")