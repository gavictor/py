from random import randint
NAleatorio = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)) # tupla randomica
print('Os números sorteados foram: ',end='')
for n in NAleatorio:
	print(n,end=' ')
print(f'\nO maior valor foi {max(NAleatorio)}')
print(f'O menor valor foi {min(NAleatorio)}')