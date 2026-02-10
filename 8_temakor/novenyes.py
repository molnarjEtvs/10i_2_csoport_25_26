import os
os.system("cls")

def viz_igeny(novenyNev:str,nedvessegTartalom:int):
    vizmennyiseg = 5.0
    if nedvessegTartalom>60:
        vizmennyiseg = 0.0
    elif nedvessegTartalom<20:
        if novenyNev.lower().strip()=="pázsit":
            vizmennyiseg = 10.0
        elif novenyNev.lower().strip() == "paradicsom":
            vizmennyiseg = 15.0
    return vizmennyiseg

def naplozas(novenyNev:str,vizmennyiseg:float):
    print(f"Öntözés: {novenyNev} megkapta a {vizmennyiseg} liter vizet.")

novenyNeve = "paradicsom"
noveny_vm_1 = viz_igeny(novenyNeve,20)
naplozas(novenyNeve,noveny_vm_1)

