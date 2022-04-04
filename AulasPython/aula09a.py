frase = 'jscnjbcsjsjvd bknfsj'
'''esse código mostra o tamanho da string da variavel'''
len(frase)
'''esse codigo do parametro, retorna onde se inicia o que está escrito na string'''
print(frase.find('cnjb'))
'''esse codigo do parametro, retorna se tem uma string especifica dentro de uma variavel'''
print('curso' in frase)
'''esse codigo do parametro retorna quantas letras(especificadas ali) têm dentro da string inserida na variável'''
print(frase.count('j'))
print(len(frase))
'''esse código do parametro simplesmente troca as strings'''
print(frase.replace('jscnjb','soudoentekkk'))
'''esse código deixa toda a string em maiusculo'''
print(frase.upper())
'''esse código deixa toda a string em minusculo'''
print(frase.lower())
'''esse código deixa somente a primeira letra maiuscula'''
print(frase.capitalize())
'''esse código deixa a primeira letra de todas palavras separadas em maiusculo'''
print(frase.title())
'''esse código remove todos os espaços inúteis, no inicio e fim da string, colocando o r ou o l na frente, indica se quero tirar somente da esquerda ou direita.'''
print(frase.strip())
'''o codigo split separa as palavras em listas, começando-as novamente  do 0'''
print(frase.split())
'''o codigo join, junta uma coisa na outra, por ex:'''
print('-'.join(frase))