import os
os.system("cls")

lista = []

for _ in range(6):
    szo = input("adj meg egy szót: ")
    if szo.isalpha() == True:
        lista.append(szo)

print(lista)