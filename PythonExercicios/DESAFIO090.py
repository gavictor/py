aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
	aluno['situação'] = 'Aprovado.'
elif aluno['média'] == 5 or aluno['média'] < 7:
	aluno['situação'] = 'Recuperação.'
elif aluno['média'] < 5:
	aluno['situação'] = 'Reprovado.'
print(f'O aluno {aluno["nome"]} teve sua média de {aluno["média"]} e sua situação é: {aluno["situação"]}')