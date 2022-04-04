preço = float(input('Digite o preço do produto: R$'))
print ('''Você vai pagar em dinheiro, cheque ou cartão à vista? 
	[1]À vista dinheiro/cheque
	[2]À vista no cartão
	[3]2x no cartão
	[4]3x ou mais no cartão''')
escolha = str(input('Sua opção: ')).strip().lower()


if escolha in '1':
	novoValor= preço - (preço* 10/100)
	print(f'O seu produto de {preço:.2f} teve um desconto de 10% à vista, o novo valor é de {novoValor:.2f}')

elif escolha in '2':
	novoValor = preço - (preço * 5/100)
	print(f'O seu produto de {preço:.2f} teve um desconto de 5% no cartão à vista, o novo valor é de {novoValor:.2f}')

if escolha in '3':
	parcelado = preço/2
	print(f'O seu produto de {preço:.2f} continua pelo mesmo valor, parcelado por {parcelado}.')
elif escolha in '4':
	parcelas = int(input('Quantas parcelas? '))
	novoValor = preço + (preço * 20/100)
	parcelado = novoValor/parcelas
	print(f'O novo valor de seu produto com juros é de {novoValor} e ficará parcelado em {parcelas}x de {parcelado:.2f}')
else:
 	print('Opção Inválida de Pagamento, tente novamente.')