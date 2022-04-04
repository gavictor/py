''' leia dois números inteiros e compare-os,  mostrando na tela uma mensagem. '''
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
	maior = n1
	print(f'O primeiro valor é maior!')
elif n2>n1:
	maior = n2
	print(f'O Segundo Valor é Maior!')
elif n1 == n2:
	print(f'Não existe valor maior, os dois são iguais')