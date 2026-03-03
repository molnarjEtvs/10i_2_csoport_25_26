import os, math
os.system("cls")

try:
    r = int(input("Add meg a sugarat:"))
    m = int(input("Add meg a magasságot:"))


except:
    print("Hibás adatbevitel")


pi = 3.14

a = math.sqrt(r ** 2 + m ** 2)
a = round(a, 2)

A = r**2*pi+r*pi*a
A = round(A,2)

V = (r**2*pi*m)/3
V = round(V,2)
print(f"A térfogat: {V}")
print(f"A felszín: {A}")
if A>=10:
    print("A felszín legalább 10")