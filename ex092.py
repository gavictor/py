import numpy as np
from datetime import date
tdcmin = 33 #tempo de contribuição mínimo
ano_atual = date.today().year
pessoa = {}
pessoa['nome'] = str(input('Seu nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['idade'] = ano_atual - pessoa['nascimento']
pessoa['ctps'] = int(input('Sua carteira de trabalho(se não tiver, 0.): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Seu ano de contratação: '))
    pessoa['salário'] = float(input('Seu salário: '))
    pessoa['aposentadoria'] = tdcmin - pessoa['idade']
    print(f'Seu nome é {pessoa["nome"]} você tem {pessoa["idade"]} anos, sua carteira de trabalho é {pessoa["ctps"]}, foi contratado em {pessoa["contratação"]} tem um salário de {pessoa["salário"]} e faltam {pessoa["aposentadoria"]} anos de contribuição para se aposentar.')
else:
    print(f'Seu nome é {pessoa["nome"]} você tem {pessoa["idade"]} anos e ainda não trabalha.')