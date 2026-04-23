import os
os.system("cls")

def macskaRogzites():
    macskak = []
    while True:
        nev =  input("Add meg a macska nevét:").capitalize()
        if not nev:
            break
        if nev not in macskak:
            macskak.append(nev)
    return macskak