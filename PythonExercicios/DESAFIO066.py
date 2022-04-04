numero = soma = contador = 0
while True:
	numero = int(input('Digite um número: '))
	if numero == 999:
		break
	contador+=1
	soma += numero
print(f'Você digitou {contador} numeros e a soma entre eles é de {soma}.')