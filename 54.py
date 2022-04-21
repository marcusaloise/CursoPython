# POO em python
# Trabalhando com classes
# o self vai atuar como objeto


import functools


class Funcionarios:

    # metodo contrutor de funcionario 
    def __init__(self,nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    # retorna o nome completo 
    def nomeCompelto(self):
        return self.nome + '' + self.sobrenome
        

# objetos criados
usuario1 = Funcionarios('Marcus', 'Aloise', '2002')
usuario2 = Funcionarios('Atila', 'Cabeça', '1992')

# mostrandos os dados dos objetos
print(usuario1.nome, usuario1.sobrenome)
print(usuario1.nomeCompelto)

print(Funcionarios.nomeCompelto(usuario1))
