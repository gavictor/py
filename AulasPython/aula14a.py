n=1
par = impar=0
while n != 0:
	n = int(input('Digite um valor: '))
	if n != 0:
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
print(f'Você digitou {par} numeros pares e {impar} impares.')



'''c=1 #o c é a variavel que representa o inicio do intervalo.
while c<10:
	print(c)
	c += 1
print('fim')'''