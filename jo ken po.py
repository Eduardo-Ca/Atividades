import random
from time import sleep

print("Bem vindo ao Jo ken po!!")
print("-"*30)
escolha = int(input("escolha pedra(1) papel(2) tesoura(3): "))


if escolha == 1 or escolha == 2 or escolha == 3:
    pass
else:
    while escolha < 1 or escolha > 3:
        print("numero inválido escolha 1,2 ou 3 !!")
        escolha = int(input("escolha pedra(1) papel(2) tesoura(3): "))

print("Agora é minha vez.")
aleatorio = random.randrange(3)
sleep(1)
print("Pronto escolhi !")

#EMPATES
if aleatorio == 1 and escolha == 1:
    print("PEDRA")
    print("EMPATE!!")
elif aleatorio == 2 and escolha == 2:
    print("PAPEL")
    print("EMPATE!!")
elif aleatorio == 3 and escolha == 3:
    print("TESOURA")
    print("EMPATE!!")

#VOCÊ VENCE
elif aleatorio == 1 and escolha == 2:
    print("PEDRA")
    print("EU PERDI =( ")
elif aleatorio == 2 and escolha == 3:
    print("PAPEL")
    print("EU PERDI =( ")
elif aleatorio == 3 and escolha == 1:
    print("TESOURA")
    print("EU PERDI =( ")

#VOCÊ PERDE
elif aleatorio == 2 and escolha == 1:
    print("PAPEL")
    print("EU VENCII !! =) ")
elif aleatorio == 3 and escolha == 2:
    print("TESOURA")
    print("EU VENCII !! =) ")
elif  aleatorio == 1 and escolha == 3:
    print("PEDRA")
    print("EU VENCII !! =) ")
