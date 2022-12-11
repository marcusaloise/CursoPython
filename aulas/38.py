# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index // perde a index quando usa o SET

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2 ) # union, ele junta os itens e tira os repetidos

print(num1 - num2) # Difference, mostra a diferença das listas

print(num1 ^ num2) #symmetric Ddifference, ele retira TODOS  os itens duplicados da lista // valores unicos

print(num1 & num2) # And, Ele mostra oque e duplicado

print(len(num1)) # mostra o tamanho do array
