from unicodedata import numeric

def padrao_brasil():
    placa_n = placa[3:7]
    placa_l = placa[0:3]
    

    if  len(placa) < 7 or len(placa) >7:
        print("")
    elif placa_n.isnumeric() and placa_l.isalpha ():
        print("padrão: Brasi")

def Padrão_mercosul():
    placa_n = placa[3]
    placa_n2 = placa[5:7]
    placa_l = placa[0:3]
    placa_l2 = placa[4]
   

    if  len(placa) < 7 or len(placa) >7:
        print("formato inválido") 
    elif placa_n.isnumeric() and placa_n2.isnumeric() and placa_l.isalpha() and placa_l2.isalpha():
        print("Padrão: Mercosul")

placa = input("Digite sua placa:")
placa = placa.upper()
print(placa)

Padrão_mercosul()
padrao_brasil()




 
   