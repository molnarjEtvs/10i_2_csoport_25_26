import os
os.system("cls")

gyumolcsok = []
while True:
    gyumolcs = input("Add meg a gyümölcs nevét: ")
    if not gyumolcs:
        break
    gyumolcs = gyumolcs.capitalize()
    gyumolcsok.append(gyumolcs)

print(gyumolcsok)