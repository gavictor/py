vel = float(input('Velocidade do carro em Km/h: '))

if vel > 80:
	print(f'Você foi multado.')
	multa = 7.00
	print(f'O valor de sua multa é {multa*(vel-80)}') 
else:
	print(f'Você está de parabéns, sem multa.')