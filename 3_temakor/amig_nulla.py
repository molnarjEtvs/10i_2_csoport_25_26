import os
os.system("cls")
#1 lehetőség
szam = 1
osszeg = 0
while szam != 0:
    szam = int(input("Adj meg egy egész számot: "))
    osszeg += szam

print(f"A számok összege: {osszeg}")

#2. lehetőség
osszeg = 0
while True:
    szam = int(input("Adj meg egy egész számot: "))
    if szam == 0:
        break
    osszeg += szam
print(f"A számok összege: {osszeg}")