import os
os.system("cls")

euro = float(input("Add meg mennyi eurod van: "))
arfolyam = int(input("Euró árfolyama: "))
forint = euro * arfolyam
print(f"{forint} -nak megfelelő eurod van")