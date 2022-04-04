soma = 0
for numeros in range(0,5):
	n1 = int(input('Digite algum valor: '))
	if n1 % 2 == 0:
		soma += n1
	else:
		print('Números Ímpares São Desconsiderados.')
print(soma)