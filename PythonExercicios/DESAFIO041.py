print("""A Confederação Nacional de Natação Precisa de Um Programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.""")
from datetime import date
anoAtual = date.today().year
anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNascimento
if idade <=  9:
	print(f'Você tem {idade} anos, é um atleta Mirim!')
elif idade <=  14:
	print(f'Você tem {idade} anos, é um atleta infantil.')
elif idade <= 19:
	print(f'Você tem {idade} anos, é um atleta junior.')
elif idade > 19 and idade < 21:
	print(f'Você tem {idade} anos, é um atleta Sênior.')
else:
	print(f'Você tem {idade} anos, é um atleta Master!')
