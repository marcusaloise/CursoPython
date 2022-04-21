# usando o try com o else e finally

# o else e apenas usado quando eu quero que algo acontece quando não der erro e finally quando der erro

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(type(valor))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
finally:
    print('Tudo certo')

# else:
#     resultado = valor * 3
#     print(resultado)
print('ele não para com o erro')

