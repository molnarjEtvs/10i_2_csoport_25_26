import os
os.system("cls")

csunyak = ["köcsög","bunkó","qrva"]
szepek = ["váza","kedves","örömlány"]

mondat = input("Adj meg egy mondatot: ")
for x in range(len(csunyak)):
    mondat = mondat.replace(csunyak[x],szepek[x])

print(mondat)