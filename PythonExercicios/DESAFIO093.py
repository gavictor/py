jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input('Quantas partidas jogou? '))
for j in range(0,tot):
	partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {j+1}?')))
	jogador['gols'] = partidas[:] # cópia dos dados da lista para o dicionário.
	jogador['total'] = sum(jogador['gols']) # sum faz uma soma sem necessariamente fazer um for.
print('-='*11)
print(jogador)
print('-='*11)
for k,v in jogador.items():
	print(f' - O valor {k} é igual a {v}')
print('-='*11)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for j in enumerate(partidas):
	print(f' => Na partida {j[0]+1} fez {j[1]} gols')
print(f'Foi um total de {jogador["total"]} gols.')
print('-='*11)
