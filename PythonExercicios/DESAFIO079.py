numeros = list() # ou pode somente abrir colchetes []
while True:
	add = (int(input('Digite algum valor: ')))
	if add not in numeros:
		numeros.append(add)
		print('Número Adicionado.')
	else:
		print(f'O número {add} já existe na lista, não vou adicionar.')

	r = str(input('Quer continuar? [S/N]: ')).strip().upper()
	if r in 'Nn':
		break
print(f'Você digitou os valores: {sorted(numeros)}')