'''refazer o exercicio 035, dessa vez informando se o triangulo é equilatero, isosceles ou escaleno'''
r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
	print('Os Segmentos Podem Formar Um Triângulo ',end='')#o end faz a linha de baixo vir para cima, pq o fim dessa está vazio!
	if r1 == r2 ==r3:
		print('EQUILÁTERO!')
	elif r1 != r2 != r3 != r1:
		print('ESCALENO!') 
	else:
		print('ISÓSCELES!')
else:
	print('Os Segmentos Não Podem Formar Um Triângulo')