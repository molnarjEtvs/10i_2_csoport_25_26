import os,random
os.system("cls")

opciok = ["K","P","O"]
gep = random.choice(opciok)
user = input("Kő (K)? Papír(P)? Olló(O)? : ")

if gep == user:
    print("Döntetlen!")
elif (gep == "K" and user == "P") or (gep == "P" and user == "O") or (gep == "O" and user == "K"):
    print("NYERTÉL!")
else:
    print("Vesztettél!")
