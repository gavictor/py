matriz = [[0,0,0],[0,0,0],[0,0,0]]
for coluna in range(0,3):
	for linha in range(0,3):
		matriz[coluna][linha] = int(input(f'Digite um valor para {coluna},{linha}: '))
for coluna in range(0,3):
	for linha in range(0,3):
		print(f'[{matriz[coluna][linha]:^5}]',end='')
	print()