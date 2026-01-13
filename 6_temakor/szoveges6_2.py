import os
os.system("cls")

szo = input("Adj meg egy szót: ")
hossz = int(input("Add meg a hosszt: "))
karakter = input("Add meg a kitöltő karaktert: ")
kozepre = szo.center(hossz,karakter)
print(kozepre)