pessoas = list()
temp = list()
maior = menor = 0
while True:
	temp.append(str(input('Seu nome: ')))
	temp.append(float(input('Seu peso: ')))
	if len(pessoas) == 0:
		maior = menor = temp[1]
	else:
		if temp[1] > maior:
			maior = temp[1]
		if temp[1] < menor:
			menor = temp[1]
	pessoas.append(temp[:])
	temp.clear()
	resposta = str(input('Você deseja continuar?[S/N]: '))[0].strip().upper()
	if resposta in 'N':
		break
print(f'{len(pessoas)} se cadastraram.')
print(f'O maior peso foi {maior} de: ',end='')
for p in pessoas:
	if p[1] == maior:
		print(f'{p[0]}...',end='')
print()
print(f'O menor peso foi {menor} de: ',end='')
for p in pessoas:
	if p[1] == menor:
		print(f'{p[0]}...',end='')