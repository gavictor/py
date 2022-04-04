numero = int(input('Digite qualquer número[999 condição de parada.]: '))
contador = 0
soma = 0
while numero != 999:
	contador += 1
	soma += numero
	numero = int(input('Digite qualquer número[999 condição de parada.]: '))
print(f'Você digitou {contador} numeros e a soma entre eles totaliza-se em: {soma}')