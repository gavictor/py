ficha = []
while True:
	nome = str(input('Seu nome: '))
	notas1 = float(input('Nota 1: '))
	notas2 = float(input('Nota 2: '))
	media = (notas1 + notas2) / 2
	ficha.append([nome,[notas1,notas2],media])

	resposta = str(input('Quer continuar?[S/N]:'))[0].strip().upper()
	if resposta in 'N':
		break
print(f'-='*10)
print(f'{"No.":<4}{"Nome":<10}{"Média":>7}')
for i,a in enumerate(ficha):
	print(f'{i:<4}{a[0]:<10}{a[2]:>7}')
while True:
	opc = int(input('Deseja ver as notas de qual aluno?(999 interrompe.): '))
	if opc == 999:
		print('Finalizando.')
		break
	if opc <= len(ficha) -1:
		print(f'as notas de {ficha[opc][0]} são {ficha[opc][1]}')
