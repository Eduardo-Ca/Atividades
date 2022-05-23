x =  int(input("escreva um numero: "))

while x != 1:
    
    resto = x % 2
    
    if resto == 0:
        x = int(x/2)
    else:
        x = int(x * 3 + 1)

    print (x)

    if x <= 0:
        break

print("fim")