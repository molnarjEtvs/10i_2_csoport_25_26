import os,random
os.system("cls")
sorszam = 1
gondolt_szam = random.randint(1,1000)
while True:
    tipp = int(input(f"Add meg a {sorszam}. tipped: "))
    sorszam+=1
    if gondolt_szam>tipp:
        print("A gondolt szám nagyobb!")
    elif gondolt_szam<tipp:
        print("A gondolt szám kisebb!")
    else:
        print("Eltaláltad a számot")
        break