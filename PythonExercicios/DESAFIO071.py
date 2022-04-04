print('='*40)
print('{:^30}'.format('Bradesco'))
print('='*40)
#variaveis
totalced = 0 #contador para atribuir a quantia de cedulas que vai sacar.
#estrutura
sacar = int(input('Quanto Você Quer Sacar?: R$')) # VARIAVEL PARA SABER QUANTO O USUARIO DESEJA SACAR.
total = sacar
cedula = 50
while True:
	if total >= 50:
		total -= cedula 
		totalced += 1 # o contador lista quantas vezes se subtrai o total do valor padrão de cedulas, definido por mim.
	else:
		if totalced > 0:
			print(f'Você tirou {totalced} cedulas de {cedula}')
		if cedula == 50:
			cedula = 20
		elif cedula == 20:
			cedula = 10
		elif cedula == 10:
			cedula = 1
		totalced = 0
		if total == 0:
			break 
print('='*30)
print('Volte Sempre Ao Banco Bradesco.')