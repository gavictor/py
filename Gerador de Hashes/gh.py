from hashlib import *
from funções import *

frase =  input('Frase para gerar o Hash em MD5: ')
while True:
	try:
		menu()
		escolha = int(input('Sua opção: '))
		if escolha == 1:
			resultado = md5(b'{frase}')
			print(f'O hash da string em MD5 é: {resultado.hexdigest()}')
		elif escolha == 2:
			resultado = sha1(b'{frase}')
			print(f'O hash da string em SHA1 é: {resultado.hexdigest()}')
		elif escolha == 3:
			resultado = sha256(b'{frase}')
			print(f'O hash da string em SHA256 é: {resultado.hexdigest()}')
		elif escolha == 4:
			resultado  = sha512(b'{frase}')
			print(f'O hash da string em SHA512 é: {resultado.hexdigest()}')
		elif escolha == 5:
			print(f'Saindo do Programa...')
			break
		else:
			print(f'Algo deu errado, tente novamente.')
	except ValueError:
			print(f'Algo deu errado, tente novamente.')
#resultado = md5(b'{frase}')
#print(f'O hash da string é: {resultado.hexdigest()}')