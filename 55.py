# POO em python
# Trabalhando com classes
# o self vai atuar como objeto


from datetime import datetime
import functools


class Funcionarios:

    # metodo contrutor de funcionario 
    def __init__(self,nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    # retorna o nome completo 
    def nomeCompelto(self):
        return self.nome + ' ' + self.sobrenome
        
    def idadeFuncionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        

# objetos criados
usuario1 = Funcionarios('Marcus', 'Aloise', 2002)
usuario2 = Funcionarios('Atila', 'Cabeça', 1992)


print(Funcionarios.nomeCompelto(usuario1))
print(Funcionarios.idadeFuncionario(usuario2))
