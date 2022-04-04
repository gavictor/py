jogador = dict()
partidas = list()
time = list()
tot = 0
while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome Do Jogador: ')).strip()
	tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
	partidas.clear()
	for c in range(0,tot):
		partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
	jogador['gols'] = partidas[:]
	jogador['total'] = sum(partidas)
	time.append(jogador.copy())
	while True:
		resposta = str(input('Quer continuar?[S/N]: '))[0].strip().upper()
		if resposta in 'SN':
			print(f'Jogador Cadastrado.')
			print('-='*13)
			break
		print(f'Opção {resposta} inválida, tente novamente.')
	if resposta == 'N':
		break
print(f'-='*16)
print('cod ',end='')
for i in jogador.keys():
	print(f'{i:<15}',end='')
print()
print('-'*25)
for k, v in enumerate(time):
	print(f'{k:>3} ',end='')
	for d in v.values():
		print(f'{str(d):<15}',end='')
	print()
print(f'-='*16)
while True:
	busca = int(input('Mostrar dados de qual jogador?(999 para parar)'))
	if busca == 999:
		break
	if busca >= len(time):
		print('Esse jogador não existe.')
	else:
		print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
		for i, g in enumerate(time[busca]['gols']):
			print(f'   no jogo  {i+1} fez {g} gols')
		print('-'*25)
print('<<< VOLTE SEMPRE! >>>')