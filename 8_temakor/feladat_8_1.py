import os
os.system("cls")

def fizetes_szamitas(oraszam:int,oraber:float,tulora_szorzo:float = 1.5):
    fizetes = 0
    if oraszam<=40:
        fizetes = oraszam*oraber
    else:
        alap = oraber*40
        tulora = (oraszam-40)*(oraber*tulora_szorzo)
        fizetes = alap+tulora
    return fizetes

normalEset = fizetes_szamitas(35,2000)
print(f"normal: {normalEset} Ft")

masodikEset = fizetes_szamitas(45,2000)
print(f"Második eset: {masodikEset} Ft")

harmadikEset = fizetes_szamitas(42,2000,2.0)
print(f"Haramdik eset: {harmadikEset} Ft")