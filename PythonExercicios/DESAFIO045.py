import random
escolha = str(input('Você quer pedra, papel ou tesoura? ')).strip().lower()
pcescolha = ['pedra','papel','tesoura']
escolhapc = random.choice(pcescolha)

if escolhapc == 'pedra':
	if escolha in 'pedra':
		print(f'O computador jogou {escolhapc} e o jogador {escolha}')
		print('Empate!')
	if escolha in 'papel':
		print(f'O computador jogou {escolhapc} e o jogador {escolha}')
		print('O jogador venceu!')
	if escolha in 'tesoura':
		print(f'O computador jogou {escolhapc} e o jogador {escolha}')
		print('O computador venceu!')
	else:
		print('Jogada inválida.')

elif escolhapc == 'papel':
	if escolha in 'papel':
		print(f'Foi um empate, o computador e o jogador jogaram {escolha}')
	if escolha in 'pedra':
		print(f'O computador jogou {escolhapc} e o jogador {escolha}, o computador venceu!')
	if escolha in 'tesoura':
		print(f'{escolha} ganha de {escolhapc}, jogador venceu.')
	else:
		print('Jogada inválida')

elif escolhapc == 'tesoura':
	if escolha in 'tesoura':
		print(f'É um empate, os dois jogaram {escolha}')
	if escolha in 'pedra':
		print(f'O jogador jogou {escolha} e o computador {escolhapc}, jogador venceu!')
	if escolha in 'papel':
		print(f'O jogador perdeu, o computador jogou {escolhapc} e você, {escolha}.')
	else:
		print('Jogada inválida')