print("oque deseja comprar? \n 1:leite R$ 2,00 \n 2:tomate R$ 4,79 \n 3:arroz R$ 40,00")

produto = int(input("\nDigite 1, 2 ou 3: "))

quantidade = float(input("quantidade? "))

if produto == 1:
    total = 2.00 * quantidade
   
    if quantidade <= 5:
        desconto = (total*5.55) / 100
    elif quantidade > 5 and quantidade <= 10:
        desconto = (total * 8.0) / 100
    elif quantidade > 10:
        desconto = (total * 12.5) /100

    total_pagar = total - desconto

if produto == 2:
    total  = 4.79 * quantidade

    if quantidade <= 5:
        desconto = (total*5.55) / 100.0
    elif quantidade > 5 and quantidade <= 10:
        desconto = float((total * 8.0) / 100.0)
    elif quantidade > 10:
        desconto = (total * 12.5) /100.0
        
    total_pagar = total - desconto

if produto == 3:
    total = 40 * quantidade
   
    if quantidade <= 5:
        desconto = (total*5.55) / 100
    elif quantidade > 5 and quantidade <= 10:
        desconto = (total * 8.0) / 100
    elif quantidade > 10:
        desconto = (total * 12.5) /100
        
    total_pagar = total - desconto



print(f"total: {total} desconto: {desconto:.2f} total a pagar: {total_pagar:.2f}")

   