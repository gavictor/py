lista = list()
cont = 0
while True:
	numero = int(input('Digite um valor: '))
	lista.append(numero)
	cont+=1
	resposta = str(input('Quer continuar?[S/N]: '))
	if resposta in 'Nn':
		break
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos')
print(f'os valores em ordem decrescente são: {lista}')
print('O valor 5 está na lista'if 5 in lista else 'O valor 5 não está na lista')