teste = 0
unica = [[],[]]
for numeros in range(0,7):
	teste = (int(input('Digite um valor: ')))
	if teste % 2 == 0:
		unica[0].append(teste)
	elif teste % 2 == 1:
		unica[1].append(teste)
unica[0].sort()
unica[1].sort()
print(f'''Os numeros pares em orderm crescente: {unica[0]} 
impares em ordem crescente é: {unica[1]}''')