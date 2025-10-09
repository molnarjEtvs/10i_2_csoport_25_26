import os
os.system("cls")

testsuly = float(input("Add meg a testsúlyod (kg): "))
mag = int(input("Add meg a magasságot (cm): "))
mag_m = mag / 100
tti = testsuly / mag_m**2

if tti<=15.99:
    print("Súlyos soványság ")
elif tti>=16 and tti <=16.99:
    print("mérsékelt soványság")

