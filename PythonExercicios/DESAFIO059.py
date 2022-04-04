n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = 0
multiplicação = 0
maior = 0
opção = 0
while opção != 5:
	print('O Que Você Deseja Fazer?')
	print('----- Menu -----')
	print('''[1] Somar
	[2]Multiplicar
		[3]Maior
			[4]Novos Números
				[5]Sair Do Programa''')
	opção = int(input('Sua opção: '))

	if opção == 1:
		soma = n1 + n2
		print(f'{soma}\n')
		
	elif opção == 2:
		multiplicação = n1 * n2
		print(f'{multiplicação}\n')
		
	elif opção == 3:
		if n1>n2:
			print(f'O maior número é {n1}\n')
			
		else:
			print(f'O maior número é {n2}\n')
			
	elif opção == 4:
		n1 = int(input('Digite um valor: '))
		n2 = int(input('Digite outro valor: '))
		print('O Que Você Deseja Fazer?')
		print('----- Menu -----')
		print('''[1] Somar
			[2]Multiplicar
				[3]Maior
					[4]Novos Números
						[5]Sair Do Programa''')
		opção = int(input('Sua opção: '))
	else:
		print('Opção Inválida, tente novamente\n')
	
print('Você saiu do programa.')
