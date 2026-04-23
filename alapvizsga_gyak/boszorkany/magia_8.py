import os,math
os.system("cls")

try:
    koncentratum = int(input("Add meg a koncentrátumot: "))
    homerseklet = float(input("Add meg a hőmérsékletet: "))
    szerencsFaktor = 1.25
    ido = math.sqrt((koncentratum+homerseklet) * szerencsFaktor)
    bankariIdo = round(ido,2)
    print(f"Kiszámolt idő: {bankariIdo}")
    if bankariIdo<10:
        print("Instabil főzet! Az üst felrobbant!")
    elif bankariIdo>=10 and bankariIdo<35:
        print("Tökéletes időzítés....")
    else:
        print("Túlfőzött lötty....")
except:
    print("számokat adj meg!")