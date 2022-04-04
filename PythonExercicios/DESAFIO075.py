'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
pares = cont= contPares = primeiroTres = 0 #contador para saber quantas vezes apareceu o 9
numeros = (int(input('Digite um valor: ')),
		   int(input('Digite outro valor: ')),
		   int(input('Digite mais um valor: ')),
		   int(input('Digite o ultimo valor: ')))


total = print(f'Você digitou {numeros}')
print(f'Apareceram {numeros.count(9)} numeros 9')
if 3 in numeros:
	print(f'O primeiro três apareceu na posição {numeros.index(3)+1}')
else:
	print('O valor três não foi digitado')
print(f'os numeros pares foram: ')
for n in numeros:
	if n % 2 == 0:
		print(n,end=' ')