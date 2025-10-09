import os
os.system("cls")

szektorAr = 6500
paholyAr = 9800
diakKedvezmeny = 0.75
vegosszeg = 0

hely = input("Hova szeretnél jegyet? Páholy (P), Szektor (S): ")
db = int(input("Mennyi jegyet szeretnél? (db):"))
diake = input("Diák vagy? Igen (i), Nem (n): ")

if hely == "P":
    vegosszeg = db*paholyAr
elif hely == "S":
    vegosszeg = db*szektorAr
else:
    print("Nincs ilyen hely")

if diake == "i":
    vegosszeg = vegosszeg*diakKedvezmeny

print(f"A végösszeg: {vegosszeg} Ft")