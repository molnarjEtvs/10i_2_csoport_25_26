import os,random
os.system("cls")

ipCim = []
for _ in range(4):
    szam = random.randint(0,255)
    ipCim.append(str(szam))
sep = "."
ip = sep.join(ipCim)

print(ip)