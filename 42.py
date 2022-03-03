# Dicionários
    # Utilizar index no formato de keys e Values
    # Aceita string, int, float, boolean


aluno = {'nome': 'Bolivar', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

print(aluno['nome'])

aluno['nome'] = 'Marcus'

print(aluno['nome'])

aluno.update({'nome': 'Rildo', 'idade': 80})

print(aluno['nome'])

aluno.update({'endereço': 'Av.calama 2896'})

print(aluno)

print(aluno.get('aprovação'))