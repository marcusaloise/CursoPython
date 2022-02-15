# Sistema de loja de tinta

cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']

corCliente = input("'Digite a cor desejada: ")

if corCliente in cores:
    print(f'Sim, temos a cor {corCliente}')
else:
    print(f'Não temos a cor {corCliente}')