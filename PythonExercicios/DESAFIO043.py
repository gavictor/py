altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura*altura)
if imc < 18.5:
	print(f'Seu imc é de {imc:.2f}, você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
	print(f'Seu imc é de {imc:.2f}, você está no peso ideal!')
elif imc >= 25 and imc <= 30:
	print(f'Seu imc é de {imc:.2f}, você está em sobrepeso.')
elif imc >= 30 and imc <= 40:
	print(f'Seu imc é de {imc:.2f}, você tem obesidade.')
elif imc > 40:
	print(f'Seu imc é de {imc:.2f}, você tem obesidade mórbida.')