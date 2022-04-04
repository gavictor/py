print('-='*11)
print('TABUADA 3.0')
print('-='*11)
#variaveis
contador = 0

#inicio do programa.
while True: # vai ter um looping infinito enquanto não houver um break
	valor = int(input('Quer ver a tabuada de qual valor? '))
	if valor < 0:
		break
	while True:
		contador += 1
		print(f'{valor}x{contador} = {valor*contador}')
		if contador == 10:
			contador=0
			break
	
print('Programa Tabuada Encerrado.')
