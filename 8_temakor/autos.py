def utikoltseg_szamitas(tavolsag:int,fogyasztas:float,benzinar:float,utasok:int=1):
    uzemanyagFogy = (tavolsag/100)*fogyasztas
    teljesKtsg = uzemanyagFogy*benzinar
    fejenkentiKtsg = teljesKtsg/utasok
    return fejenkentiKtsg