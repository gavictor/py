nome = 'Gabriel'
cores =  {'limpa':'\033[m',
		'azul':'\033[34m',
		'amarelo':'\033[33m'}
print(f'Olá, prazer em te conhecer, {cores["azul"]}{nome}{'\033[m'}')