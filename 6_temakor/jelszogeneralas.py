import os,random
os.system("cls")

karakterek = "qwertzuiopasdfghjklyxcvbnm0123456789QWERTZUIOPASDFGHJKLYXCVBNM"
karakterLista = list(karakterek)
db = int(input("Add meg a jelszó hosszát: "))
jelszo = ""
for _ in range(db):
    i = random.randint(0,len(karakterLista)-1)
    karakter = karakterLista[i]
    jelszo += karakter

print(jelszo)
