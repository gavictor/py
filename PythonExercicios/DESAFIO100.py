from time import sleep
from random import randint
def sorteia(lista):
	for c in range(0,5):
		nsort = randint(0,10)
		lista.append(nsort)
		print(f'{nsort} ',end='',flush=True)
		sleep(0.6)


def soma_pares(lista):
	soma = 0
	for valores in lista:
		if valores % 2 == 0:
			soma += valores
	print(f'\nO total da soma de valores pares é de: {soma}')

numeros = list()
soma = nsort = 0
sorteia(numeros)
soma_pares(numeros)