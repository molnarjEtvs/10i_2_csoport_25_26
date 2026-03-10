import os
os.sytem("cls")


def orszagRogzites():
    orszagok=[]
    while True:
        orszag = input("Adjon meg egy orzságnevet: ").capitalize()
        if orszag == "":
            break
        orszagok.append(orszag)
    return orszagok

def orszagstatisztika(orszagok:list):
    orszagok_db = len(orszagok)

    print(f"{orszagok_db}db ország van")
    sldb= 0
    for x in orszagok:
        if x.find("s") >-1 and x.find("l") >-1:
            sldb+=1
    szoveg = "-".join(orszagok)
    print(f"Rövzített országok: {orszagok}")
rogzitett = orszagRogzites()
orszagstatisztika(rogzitett)
