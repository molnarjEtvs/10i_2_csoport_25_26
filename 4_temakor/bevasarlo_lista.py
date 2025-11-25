import os
os.system("cls")

termekek = []
sorszam = 1
while True:
    termek = input(f"add meg a(z){sorszam}. terméket: ")
    sorszam += 1
    if not termek:
        break

torlendo = input("Add meg mit szeretnél törölni: ")
if torlendo in termekek:
    termekek.remove(torlendo)
    print(f"{torlendo} törölve lett")
else:
    print("Nincs ilyen termék a listában")

sorszam = 1
for termek in termekek:
    print(f"{sorszam}. {termek}")
    sorszam += 1
