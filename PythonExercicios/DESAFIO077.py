palavras = (
			'Mercado',
			'Programador',
			'Futuro',
			'Curso',
			'Altruismo',
			'Linguagem',
			'Aprender',
			'Padrao')
for p in palavras:
	print(f'\nna palavra {p} temos: ',end=' ')
	for letra in p:
		if letra.upper() in 'A E I O U':
			print(letra,end=' ')