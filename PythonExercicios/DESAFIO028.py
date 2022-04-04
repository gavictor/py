from random import randint
from time import sleep
n = randint(0,5) #faz o computador "PENSAR"
print('-=-'*10)
print('Pensando num número entre 0 e 5...')
print('-=-'*10)
sorte = int(input('Em que número eu pensei? '))#jogador tenta adivinhar
print('Processando...')
sleep(2)
if sorte == n:
	print(f'Parabéns, você acertou!')
else:
	print(f'Você errou :(, pensei no {n}')