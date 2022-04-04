'''Todo número ímpar, quando dividido por 2, deixa resto igual a 1'''
n1 = int(input('Digite um número: '))
par = n1 % 2

if par == 0:
	print(f'{n1} é par')
else:
	print(f'{n1} é impar.')