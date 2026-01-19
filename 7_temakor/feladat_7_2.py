import os
os.system("cls")

szoveg = input("Adj meg egy szöveget: ")
betuk = {}

for betu in szoveg:
    if betu in betuk:
        betuk[betu] += 1
    else:
        betuk[betu] = 1

'''
e:3db
z:2db
 :3db
'''

for kulcs,ertek in betuk.items():
    print(f"{kulcs}:{ertek} db")