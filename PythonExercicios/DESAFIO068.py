from random import randint
from time import sleep
print('Vamos Jogar Par Ou Impar!')
soma = 0
contador = 0
while True:
	print('Estou pensando num número...')
	escolha_computador = randint(0,1000)
	sleep(1)
	escolha_jogador = int(input('Digite um número: '))
	soma += escolha_computador + escolha_jogador
	par_impar = str(input('Par ou Impar?[P]/[I]: '))[0].strip().upper()
	if par_impar in 'pP': # JOGADOR ESCOLHEU PAR
		if soma % 2 == 0:
			contador+=1
			print(f'O computador escolheu {escolha_computador} e você {escolha_jogador}, total de {soma} que é PAR! você venceu')
			soma = 0
		else:
			print(f'O computador escolheu {escolha_computador} e você {escolha_jogador}, total de {soma} que é IMPAR! você perdeu. Ganhou {contador} vezes.')
			break
	if par_impar in 'iI':
		if soma % 2 == 1:
			contador+=1
			print(f'O computador escoclheu {escolha_computador} e você {escolha_jogador}, total de {soma} que é IMPAR! você venceu')
			soma = 0
		else:
			print(f'O computador escolheu {escolha_computador} e você {escolha_jogador}, total de {soma} que é PAR! você perdeu. Ganhou {contador} vezes.')
			break
print('Jogo Encerrado.')