# Criar uma função que soma  | xargs

def soma(*numeros):
    resultado = 0 
    for num in numeros:
        resultado += num
    return resultado


x = soma(2,3,4,10)
print(x)
