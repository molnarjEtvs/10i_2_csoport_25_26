import os
os.system("cls")

szam = int(input("Add meg a számot: "))

if szam%3 == 0:
    print(f"A {szam} osztható 3-al")
else:
    print("Nem osztható")