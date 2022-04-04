#incompleto
soma = 0
cont = 0
for impares in range(1,501,2):
	if impares % 3 == 0:
		soma += impares
		cont = cont + 1
print(f'a soma de todos os {cont} valores tem o total de {soma}')