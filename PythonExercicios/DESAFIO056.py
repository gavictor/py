MIHomens = 0 # maior idade dos homens
QMulheres = 0 # quantia  de mulheres
IGrupo = 0 # idade do grupo
MVelho = 0 # o homem mais velho

for p in range(1,5):
	print(f'----- {p}ª Pessoa -----')
	pessoa = str(input(f'Nome da {p}ª pessoa: ')).strip().lower()
	idade = int(input(f'Idade da {p}ª pessoa: '))
	IGrupo = (IGrupo + idade) / p
	genero = str(input(f'Genero da {p}ª pessoa [M]/[F]: ')).strip().lower()
	
	if genero in 'f':
		if idade < 20:
			QMulheres += 1

	if genero in 'm':
		if pessoa == 1:
			MIHomens = idade
		else:
			if idade > MIHomens:
				MIHomens = idade
print(f'A maior idade entre homens é de {MIHomens} anos')
print(f'quantia de mulheres abaixo de 20 anos é de {QMulheres}')
print(f'a média de idade do grupo é de {IGrupo} anos')