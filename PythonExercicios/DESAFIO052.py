'''faça um programa que leia um número inteiro e diga se ele é ou não um número primo '''
import colorama
from colorama import Fore
n1 = int(input('Digite um número inteiro: '))
total = 0
colorama.init()
for nPrimo in range(1,n1+1):
	if n1 % nPrimo == 0 and n1 % n1 == 0:
		total += 1
		print(f'{Fore.GREEN}')
		print(f'{n1} é um número primo')
	else:
		print(Fore.RED)
print(f'o número {n1} foi divísivel {total} vezes')
if total == 2:
	print('é um número primo.')
else:
	print('não é um número primo')