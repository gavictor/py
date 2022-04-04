from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
jogadores = {
	'jogador 1':randint(0,6),
	'jogador 2':randint(0,6),
	'jogador 3':randint(0,6),
	'jogador 4':randint(0,6)
}
for k, v in jogadores.items():
	print(f'{k} jogou {v}')
	sleep(1)
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
	print(f'Na posição {i+1} ficou o {v[0]} com: {v[1]}')
	sleep(1)