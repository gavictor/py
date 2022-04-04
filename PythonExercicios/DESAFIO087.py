matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapares = 0
maiorl2 = 0
soma3coluna = 0
for linha in range(0,3):
	for coluna in range (0,3):
		matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha,coluna}: '))
		if matriz[linha][coluna] % 2 == 0:
			somapares += matriz[linha][coluna]

for linha in range(0,3):
	for coluna in range(0,3):
		print(f'[{matriz[linha][coluna]:^5}]',end='')
	print()
for coluna in range(0,3):
	soma3coluna += matriz[coluna][2]
print(f'a soma dos valores pares foi {somapares}')
print(f'a soma da terceira coluna foi {soma3coluna}')
for linha in range(0,3):
	if linha == 0:
		maiorl2 == matriz[1][linha]
	elif matriz[1][linha]>maiorl2:
			maiorl2 = matriz[1][linha]
print(f'o maior valor da segunda linha é {maiorl2}')