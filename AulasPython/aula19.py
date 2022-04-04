estado = dict()
brasil = list()
for c in range(0,3):
	estado['uf'] = str(input('Unidade Federativa: '))
	estado['sigla'] = str(input('Sigla do Estado: '))
	brasil.append(estado.copy()) # usa o copy para copiar os dados de dicionario sem fatiamento ([:])
for e in brasil:
	print(e)


'''
Brasil = []
estado1 = {'UF':'Bahia','Sigla':'BA'}
estado2 = {'UF':'São Paulo', 'Sigla':'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil[0]['UF'])
'''

'''
pessoas = {'nome':'Gabriel','sexo':'M','idade':16}
pessoas['peso'] = 88 # pode adicionar novos values dessa maneira
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values(): #para imprimir itens, precisa do k e v, de key e value.
	print(k)
'''