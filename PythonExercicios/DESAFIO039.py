from datetime import date

print('''Você é homem ou mulher?
	[H]Para Homem
	[M]Para Mulher''')
opção = str(input('Sua opção: ')).strip().upper()
if opção in 'M':
	print('O Alistamento Não É Obrigatório Para Mulheres!')
	exit()

nascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
if idade == 18:
	print(f'Você tem {idade} anos, deve se alistar IMEDIATAMENTE!')
elif idade < 18:
	saldo = 18 - idade
	print(f'Você tem {idade} anos, ainda irá se alistar daqui a {saldo} ano(s)!')
elif idade > 18 and idade <= 45:
	saldo = idade  - 18
	print(f'Você tem {idade} anos, já passou do tempo de alistamento há {saldo} ano(s).')
else:
	print(f'Você tem {idade} anos, já passou do tempo de alistamento.')