galera = list()
dado = list()
for c in range(0,3):
	dado.append(str(input('Seu nome: ')))
	dado.append(int(input('Sua idade: ')))
	galera.append(dado[:])
	dado.clear()

for p in galera:
	if p[1] >= 21:
		print(p) #o teste lógico é feito no p, então imprime p, não galera.



'''galera = [ ['João', 19], [ 'Pedro' , 22], ['Gabriel',16], ['Clarice',49] ]
galera.sort()
for pessoa in galera:
	print(f'{pessoa[0]} Tem {pessoa[1]} Anos de Idade.') # isso é, nesse exemplo, estou pedindo para dizer o nome de todos, sem a idade, caso coloque o [1], aparece somente a idade(de todoss)
'''