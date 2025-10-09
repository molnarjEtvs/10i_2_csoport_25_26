import os
os.system("cls")

szam = int(input("Add meg a számot: "))

if szam%3==0 and szam%5==0:
    print("Mindekettővel")
elif szam%3==0:
    print("csak 3al")
elif szam%5==0:
    print("csak 5-el")
else:
    print("egyikkel sem")