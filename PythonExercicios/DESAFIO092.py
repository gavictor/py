from datetime import date
tdcmin = 35
ano_atual = date.today().year
pessoa = {}
pessoa['nome'] = str(input('Seu nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['idade'] = ano_atual - pessoa['nascimento']
pessoa['ctps'] = int(input('Sua carteira de trabalho(se não tiver, 0.): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Seu ano de contratação: '))
    pessoa['salário'] = float(input('Seu salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - ano_atual)
    print(f'Seu nome é {pessoa["nome"]} você tem {pessoa["idade"]} anos, sua carteira de trabalho é {pessoa["ctps"]}, foi contratado em {pessoa["contratação"]} tem um salário de {pessoa["salário"]} e vai se aposentar com {pessoa["aposentadoria"]} anos.')
else:
    print(f'Seu nome é {pessoa["nome"]} você tem {pessoa["idade"]} anos e ainda não trabalha.')