# Dicionários
    # Utilizar index no formato de keys e Values
    # Aceita string, int, float, boolean


aluno = {'nome': 'Bolivar', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for x in aluno.values():
    print(x)


for keys, values in aluno.items():
    print(keys, values)