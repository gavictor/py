lista = list()
maior = menor = 0
for c in range(0,5):
	lista.append([int(input('Digita uns números aí: '))]) # nunca se esquecer do append ao adicionar qualquer coisa numa lista.
	if c == 0:
		maior = menor = lista[c]
	elif lista[c] > maior:
		maior = lista[c]
	elif lista[c] < menor:
		menor = lista[c]
print(f'O maior número foi {maior} e sua posição foi ',end='')# index acha a posição da coisa na lista
for posição,v in enumerate(lista):
	if v == maior:
		print(f'{posição}... ',end='')
print()
print(f'O menor número foi {menor} e sua posição foi {lista.index(menor)}')