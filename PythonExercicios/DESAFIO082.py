listanumeros = []
pares = list()
impares = list()
while True:
	numeros = int(input('Digite um número: '))
	listanumeros.append(numeros)
	if numeros % 2 == 0:
		pares.append(numeros)
	elif numeros % 2 == 1:
		impares.append(numeros) 
	resposta = str(input('Quer continuar?[S/N]: ')).strip().upper()
	if resposta in 'nN':
		break
print()
print('-='*30)
print(f'A lista completa é: {listanumeros}')
print(f'Os números pares da lista são: {pares}')
print(f'Os números impares da lista são: {impares}')