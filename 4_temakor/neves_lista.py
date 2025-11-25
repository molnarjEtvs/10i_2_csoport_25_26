import os
os.system("cls")

nevek = []

while True:
    nev = input("Adj meg egy nevet: ")
    if not nev:
        break
    nevek.append(nev)

print(f"Első: {nevek[0]}")
print(f"Utolsó: {nevek[-1]}")
