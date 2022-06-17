valor_hora = float(input("Digite valor da hora trabalhada: "))   
horas_trabalhadas = float(input("Digite as horas trabalhadas por dia: "))
dias_trabalhadas = int(input("Digite os dias trabalhados no mês: "))

salario_bruto =  (horas_trabalhadas * dias_trabalhadas) * valor_hora
desconto = (salario_bruto * 21) / 100
salario_liquido = salario_bruto  - desconto

print(f"seu salario bruto é: R${salario_bruto:.2f}")

print(f"seu salario liquido é: R${salario_liquido:.2f}")

