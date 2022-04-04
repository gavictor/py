NExtensos = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte') # tupla com numeros extensos.
c = -1
while c > 20 or c < 0:
	c = int(input('Um número de 0 a 20: '))
	print(f'Você digitou o número {NExtensos[c]}')
	if c > 20 or c < 0:
		print('Opção Inválida, Tente novamente.')
	continuar_ou_não = ' '
	while True:
		continuar_ou_não = str(input('Deseja Continuar?[S/N]: '))[0].strip().upper()
		while continuar_ou_não in 'S':
			c = int(input('Um número de 0 a 20: '))
			print(f'Você digitou o número {NExtensos[c]}')
			continuar_ou_não = str(input('Deseja Continuar?[S/N]: '))[0].strip().upper()
			if c > 20 or c < 0:
				print('Opção Inválida, Tente novamente.')
		if continuar_ou_não in 'N':
			break
print(f'Você digitou o número {NExtensos[c]}')