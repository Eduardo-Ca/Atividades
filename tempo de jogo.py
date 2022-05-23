inicio, fim =map(int, input("escreva o Início e o fim: ").split())
print(inicio)
print(fim)

tempo = inicio - fim

if tempo <=0:
    tempo += 24

print(f"o jogo durou {tempo} horas")