import os
os.system("cls")

szo = input("Adj meg egy szót: ")
db = int(input("Adj meg egy darabszámot: "))

for sorszam in range(1,db+1):
    print(f"{sorszam}. {szo}")

