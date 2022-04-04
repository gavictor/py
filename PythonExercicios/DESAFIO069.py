contador_maior_18_anos = 0
contador_homens = 0
mulheres_abaixo_de_20_anos = 0
while True:
 	idade = int(input('Sua Idade: '))
 	sexo= ' '
 	while sexo not in 'MF':
 		sexo = str(input('Sexo [M]/[F]: '))[0].strip().upper()
 	
 	if idade > 18:
 		contador_maior_18_anos += 1
 	if sexo in 'Mm':
 		contador_homens += 1
 	if sexo in 'Ff':
 		if idade < 20:
 			mulheres_abaixo_de_20_anos += 1
 	continuar_ou_não = ' '
 	while continuar_ou_não not in 'SN':
 		continuar_ou_não = str(input('Você deseja continuar? [S]/[N]: '))[0].strip().upper()
 	if continuar_ou_não in 'Ss':
 		print('-'*13)
 		print('Uma Pessoa Cadastrada!')
 		print('-'*13)
 	if continuar_ou_não in 'Nn':
 		break
print(f'Têm {contador_maior_18_anos} pessoas maior de 18 anos\n{contador_homens} homens foram cadastrados\ntêm {mulheres_abaixo_de_20_anos} mulheres abaixo dos seus 20 anos de idade.')