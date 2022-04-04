primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
décimo = primeiro*razão*10
while cont <= 10:
	print(termo,end='->')
	termo += razão
	cont += 1
print('Acabou')