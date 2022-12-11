# Filter Function
    # Muito Utilizado com listas
    # Aplicar uma função a um int, Filtrando os itens. (Lista, tuple, dic.)

valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))


print(list(filter(lambda x: x > 20, valores)))