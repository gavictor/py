''' leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal '''

n1 = int(input('Digite um número inteiro qualquer: '))
print("""Escolha uma das bases para conversão:
	[1]Binário
	[2]Octal
	[3]Hexadecimal""")
opção = int(input('Sua opção: '))
if opção == 1:
	print(f'{n1} convertido para Binário é {bin(n1)[2:]}')
elif opção == 2:
	print(f'{n1} convertido para Octal é {oct(n1)[2:]}')
elif opção == 3:
	print(f'{n1} convertido para Hexadecimal é {hex(n1)[2:]}')
else:
	print('Opção Inválida!')