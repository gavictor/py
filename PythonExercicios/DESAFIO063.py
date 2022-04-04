print('~~'*11)
print('Sequência De Fibonacci')
print('~~'*11)
n = int(input('Quantos termos deseja mostrar?'))
t1 = 0
t2 = 1
cont = 3
print(f'{t1}->{t2}',end='->')
while cont <= n:
	t3 = t1+t2
	print(t3,end='->')
	t1 = t2
	t2 = t3
	cont += 1
print('Fim')