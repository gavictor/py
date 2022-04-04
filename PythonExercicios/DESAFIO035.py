'''Condição de existência de um triângulo
Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.'''
reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))
maior = reta3
soma = reta1 + reta2
if reta2>reta3 and reta2>reta1:
	maior = reta2
	soma = reta3+reta1 
if reta1 > reta3 and reta1>reta2:
	maior = reta1
	soma = reta2 + reta3
if soma > maior:
	print(f'Formam um triângulo')
else:
	print(f'Não formam um triângulo')