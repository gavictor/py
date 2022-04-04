nome_do_produto = ''
preço_do_produto = soma_preço = produtos_acima_de_1000 = menor_preço = contador = 0
barato = ' '
f = 'Fim do Programa'
print('~~'*11)
print('Loja Super Baratão')
print('~~'*11)
while True:
	nome_do_produto = str(input('Nome do Produto: ')).strip().capitalize()
	preço_do_produto = float(input('Preço do Produto: R$'))
	contador += 1
	soma_preço += preço_do_produto

	if preço_do_produto > 1000:
		produtos_acima_de_1000 += 1

	if contador == 1:
		menor_preço = preço_do_produto
		barato = nome_do_produto
	else:
		if preço_do_produto < menor_preço:
			barato = nome_do_produto
			menor_preço = preço_do_produto


	continuar_ou_não = ' '
	while continuar_ou_não not in 'SN':
		continuar_ou_não = str(input('Quer continuar? [S]/[N]: '))[0].strip().upper()
	if continuar_ou_não in 'N':
		break
print('--'*13)
print(f'{f:^30}')
print(f'O total da compra foi: R${soma_preço}')
print(f'Temos {produtos_acima_de_1000} produtos acima de 1000 R$')
print(f'O Menor Valor foi do produto {barato} de {menor_preço}R$ e o maior foi de {maior_preço}R$')