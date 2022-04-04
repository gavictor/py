n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m}')
if m <= 5:
	print(f'A média do colégio é 6, você está reprovado.')
else:
	print(f'Você tirou {m}, está aprovado!')