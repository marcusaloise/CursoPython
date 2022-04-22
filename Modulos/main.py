from functions import somar, mulit, procuraIndex
import functions 
from itens.cadastro import cadastroCliente
# 
# o import usa pega todos os modulos de uma vez, para burlar isso da pra usar o from <nome do modulo> import <nome da função>
# Trabalhando com modulos

functions.somar()
functions.mulit()

cadastroCliente()

list1 = ['a', 'b', 'c', 'd', 'e']

procuraIndex = procuraIndex(list1, 'b')

print(procuraIndex)
