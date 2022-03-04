# lamba Function
    # É uma função pequena sem nome
    # Pode ter vários argumentos mas somente uma expressão
    # Muito utilizado dentro de outras funções
    # código mais limpo

def somar(x):
    result = lambda x: x + 10
    return result(2) * 4
        
print(somar(2))

