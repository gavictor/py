from random import randint
from time import sleep
lista = []
sorteio = []
num = 0
jogos = int(input('Quantos jogos você quer sortear? '))
tot = 1
print('-='*11,f'Sorteando {jogos} jogos','-='*11)
while tot <= jogos:
	contador = 0
	while True:
		num = randint(1,60)
		if num not in lista:
			lista.append(num)
			contador += 1
		if contador >= 6:
			break
	lista.sort()
	sorteio.append(lista[:])
	lista.clear()
	tot+=1
for p,n in enumerate(sorteio):
	print(f'Jogo {p+1}: {n}')
	sleep(0.8)