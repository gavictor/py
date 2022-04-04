from datetime import date
anoAtual = date.today().year
Pmenor = 0
Pmaior = 0
for pessoas in range(1,7+1):
	nascimento = int(input('Em que ano você nasceu? '))
	idade = anoAtual - nascimento
	if idade < 18:
		Pmenor += 1
		
	if idade >= 18:
		Pmaior += 1
		
print(f'{Pmenor} não atingiram a maioridade')
print(f'{Pmaior} atingiram a maioridade')