import os
os.system("cls")

class Macska:

    def __init__(self,nev:str,suly:float,ehes:bool):
        self.nev = nev
        self.suly = suly
        self.ehes = ehes

    def eszik(self,etelMennyiseg:float):
        if self.ehes == True:
            self.suly += etelMennyiseg
            self.ehes = False
            return True
        else:
            return False
        
    def futkos(self):
        self.suly -= 0.1
        if self.ehes == False:
            self.ehes = True
    
    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly}")
        if self.ehes == True:
            print(f"Állapot: ÉHES")
        else:
            print(f"Állapot: NEM éhes")
    

macska1 = Macska("Cirmos",4.5,True)
if macska1.eszik(0.32) == True:
    print(f"Evett a cica {macska1.nev}")
else:
    print(f"Nem evett a cica {macska1.nev}")
macska1.futkos()

macska2 = Macska("Garfield",9.2,False)
if macska2.eszik(2.32) == True:
    print(f"Evett a cica {macska2.nev}")
else:
    print(f"Nem evett a cica {macska2.nev}")
macska2.futkos()

macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()
