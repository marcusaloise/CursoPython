
# dafault tem que ser sempre por ultimo, para que as non-defult sejam defininas pelo user

def boasVindas1():
    nome = input('Digite o seu nome: ')
    print(f'Olá {nome}.')


def boasVindas2(nome='marcus'):
    #nome = input('Digite o seu nome: ')
    print(f'Olá {nome}.')
    

#boasVindas1()
boasVindas2()



