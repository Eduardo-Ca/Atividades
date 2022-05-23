import random 

maiorValor = 0
cont = 0
valorAgua = 0

n = int(input("Digite a quantidade de apartamentos: " ))

while n > 0:

    valorAgua = round(random.random()*10000)
    print ("Apartamento ", n  ,":", valorAgua)
   
    n -= 1	
    
    if cont==0 :
        maiorValor = valorAgua
        cont += 1
	
    elif valorAgua > maiorValor:			
	    maiorValor = valorAgua	

cubico = int(maiorValor) / 1000	 

print("o Maior Valor em metros cúbicos é : " , cubico)
print("o Maior Valor  é : " , maiorValor)