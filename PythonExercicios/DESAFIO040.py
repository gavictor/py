nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m =  (nota1+nota2)/2
print(f'sua média é {m}')
if m < 5.0:
	print(f'Você foi reprovado.')
elif m >= 5.0 and m <= 6.9:
	print(f'Você está de recuperação.')
else:
	print(f'Você está aprovado!')