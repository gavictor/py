nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'Gabriel':
	print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
	print(f'Seu nome é bem popular no Brasil, {nome}')
elif nome in 'Ana Cláudia Jéssica Juliana': #aqui mostra a mensagem pra qualquer um dos nomes que esteja listado na string.
	print(f'Belo nome feminino, {nome}')
else:
	print(f'Seu nome é bem normal, {nome}')
print(f'Tenha um bom dia, {nome}')