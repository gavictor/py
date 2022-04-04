galera = []
pessoa = {}
soma = média = 0
while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Seu nome: '))
	while True:
		pessoa['sexo'] = str(input('Sexo[M/F]: '))[0].upper()
		if pessoa['sexo'] in 'MF':
			break
		print('Opção Inválida.')
	pessoa['idade'] = int(input('Sua idade: '))
	soma += pessoa['idade']
	galera.append(pessoa.copy())
	while True:
		resposta = str(input('Deseja continuar?[S/N]: '))[0].upper()
		if resposta in 'SN':
			break
		print('Opção Inválida')
	if resposta == 'N':
		break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'a média de idade é de {média:5.2f} anos.')
print(f'as mulheres cadastradas foram ',end='')
for p in galera:
	if p['sexo'] == 'F':
		print(f'{p["nome"]}',end=' ')
print()
print(f'As pessoas com idade acima da média são ',end='')
for i in galera:
	if i["idade"] > média:
		print(f'{i["nome"]}',end=' ')
