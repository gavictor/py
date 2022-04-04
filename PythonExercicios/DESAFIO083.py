expressão = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expressão:
	if simbolo == '(':
		pilha.append('(')
	elif simbolo == ')':
		if len(pilha) > 0: # se o tamanho da pilha for maior que zero
			pilha.pop()    #vai retirar o último número.
	else:
		pilha.append(')')
		break
if len(pilha) == 0:
	print('Sua expressão é válida.')
else:
	print('Sua expressão está incorreta.')