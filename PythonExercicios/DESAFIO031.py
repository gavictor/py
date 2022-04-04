distancia = float(input('E aí, usuário! Qual a distância de sua viagem em Km? '))
print('Vamos calcular o preço de sua passagem.')
if distancia <= 200:
	print(f'O preço de sua passagem é {distancia*0.50}R$')
elif distancia > 200:
	print(f'O preço de sua passagem é {distancia*0.45}R$')