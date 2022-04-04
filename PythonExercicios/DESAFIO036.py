'''
O Programa Vai Perguntar o Valor da Casa, Saláriodo comprador e Em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o emprestimo será negado.
'''

print('-=-'*12)
print('Empréstimo Bancário!')
print('-=-'*12)

casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Quanto você recebe? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

porcentagem = (salario * 30 / 100)
prestação = (casa / anos) / 12

if prestação>porcentagem:
	print('O Empréstimo Foi Negado')
else:
	print('Seu Empréstimo foi aprovado!')
	print(f'Você vai pagar {prestação:.2f} Mensais em {anos} anos.')