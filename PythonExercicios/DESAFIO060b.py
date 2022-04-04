from time import sleep
num = int(input('digite o número para calcular seu fatorial: '))
f = 1
print('Calculando...')
sleep(1)
for fatorial in range(num,0,-1):
	print(f'{fatorial}',end='')
	print(' x ' if fatorial > 1 else ' = ',end='')
	f *= fatorial
print(f'{f}')