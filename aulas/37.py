from array import array

#Array
    # Similar a listas
    # Melhor perfomance

letras = ['a','b','c','d']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

letras = array('u', ['a','b','c','d'])

numeros_i = array('i', [10, 20, 30, 40])

numerps_f = array('f', [1.2, 2.2, 3.2])
print(letras)