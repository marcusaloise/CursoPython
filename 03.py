import datetime
# crianco programa que calcula a idade de acordo com o ano de nascimento

from datetime import datetime


ano_nascimento = input('Qual foi o ano que você nasceu? ')
ano_nascimento = int(ano_nascimento)
data = (datetime.today().strftime('%Y'))
data = int(data)
idade = data - ano_nascimento

print(idade)