from random import randint
import time
tentativas = 1
escolhapc = randint(1,10)
print('Estou pensando num número')
time.sleep(0.5)
print('...')
time.sleep(0.5)
escolhaU = int(input('Tente acertar: ')) #escolha do usuario
while escolhaU != escolhapc:
	tentativas += 1
	print('Errou!')
	time.sleep(0.6)
	escolhaU = int(input('Tente novamente:'))
print(f'Você ganhou depois de {tentativas} tentativas, pensei em {escolhapc}')