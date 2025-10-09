import os
os.system("cls")

szam = int(input("Add meg a számot: "))
if szam%2 == 0:
    print(f"A {szam} PÁROS")
else:
    print(f"A {szam} PÁRATLAN")