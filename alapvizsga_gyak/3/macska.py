import os
os.system("cls")

try:
    kor = int(input("Add meg a cica életkorát:"))
    suly = float(input("Add meg cica súlyát:"))
    adag = 65
    hetiEtel = suly*adag*7
    if kor < 2:
        kcal = 80
    elif kor >= 2 and kor<5:
        kcal = 95
    else:
        kcal = 110
    
    mozgasIgeny = round(suly*kcal,1)

    print(f"A macska heti étel szükseglete :{hetiEtel}g ")
    print(f"A macska napi  mozgasigénye: {mozgasIgeny}kcal")
except:
    print("Rossz adattípus")

