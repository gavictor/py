contador = 0
média = 0
soma = 0
escolha = 'S'
maior = 0
menor = 0
while escolha != 'N':
	numero = int(input('Digite um número: '))
	contador += 1
	soma += numero
	if contador == 1:
		maior=menor=numero
	else:
		if numero > maior:
			maior = numero
		if numero < menor:
			menor = numero
	escolha = str(input('Deseja Continuar?[S]/[N]: ')).strip().upper()
média = soma/contador
print(f'''{contador} numeros foram digitados e a média entre os números é de {média}
	o maior número foi {maior} e o menor foi {menor}''')