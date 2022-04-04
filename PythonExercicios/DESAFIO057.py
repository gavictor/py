print('''Seu Sexo é Masculino ou Feminino?
	[M]
	[F]''')
sexo = str(input('Sua opção:')).strip().lower()[0]
#while sexo not in 'MmFf'
while sexo != 'm':
	if sexo in 'f':
		print('É uma usuária feminina.')
		exit()
	print('Resposta inválida, usuário.')
	sexo = str(input('Digite novamente: ')).strip().lower()[0]
print('É Um Usuário Masculino!')