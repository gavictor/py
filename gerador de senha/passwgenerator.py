from random import *
from string import *

while True:
	tamanho = input(f'Digite o tamanho de senha que você deseja(Recomendado entre 8 e 16 caracteres): ')
	if not tamanho.isnumeric():
		print(f'Essa opção é inválida, por favor, tente novamente.')
	else:
		valor = int(tamanho)
		break

caracteres = ascii_letters + digits + 'çÇ!@#$%&*()-=+,.:;?'

aleatorio = SystemRandom() #os.urandom, gera números aleatórios

print(f''.join(aleatorio.choice(caracteres) for i in range(valor)))
