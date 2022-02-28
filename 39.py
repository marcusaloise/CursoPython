# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index // perde a index quando usa o SET

s1 = {1, 2, 2, 3, 4, 5, 6}
s1.update([7, 8, 9, 10])
s1.remove(6) # Gera erro se por valor inexistente 
s1.discard(9)

print(s1)