maior = 0
menor = 0
for pessoas in range(1,6):
	peso = float(input(f'peso da {pessoas}ª pessoa em KG: '))
	if pessoas == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso 
		if peso < menor:
			menor = peso
print(f'o maior peso foi {maior} e o menor foi {menor}')