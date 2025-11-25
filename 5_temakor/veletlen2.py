import os,random
os.system("cls")

kettovel = []
harommal = []
ottel = []

for _ in range(30):
    vszam = random.randint(300,1500)
    if vszam%2==0:
        kettovel.append(vszam)
    if vszam%3==0:
        harommal.append(vszam)
    if vszam%5==0:
        ottel.append(vszam)

print(f"Kettővel:\n {kettovel}")
print(f"Hárommal:\n {harommal}")
print(f"Öttel:\n {ottel}")
