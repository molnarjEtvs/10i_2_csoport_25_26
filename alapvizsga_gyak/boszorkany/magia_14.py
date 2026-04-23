
def atkok_gyujtese():
    atkok = []
    while True:
        atok = input("adj meg egy átkot: ").upper()
        if not atok:
            break
        atkok.append(atok)
    return atkok

def atkokElemzese(atkok:list):
    db = len(atkok)
    print(f"{db}db átkot rögzítettel!")
    sdb = 0
    for atok in atkok:
        if atok.startswith("S") == True and atok.endswith("S") == True:
            sdb += 1
    print(f"s betűsek száma: {sdb} db")
    atokSzoveg = "<\>".join(atkok)
    print(atokSzoveg)

a = atkok_gyujtese()
atkokElemzese(a)