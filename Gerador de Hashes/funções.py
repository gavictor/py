def menu():
	lista = ['MD5', 'SHA1', 'SHA256', 'SHA512', 'Sair do Programa']
	print(f'-'*42)
	print(f'{" Menu - Escolha o tipo de Hash ".center(42)}')
	print(f'-'*42)
	c = 1
	for i in lista:
		print(f'\t{c} - {i}')
		c += 1