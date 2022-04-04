nu1 = int(input('Digite um número de 0 a 9999: '))
u = nu1 // 1 % 10
d = nu1 // 10  % 10
c = nu1 // 100 % 10
m = nu1 // 1000 % 10
print(f'analisando o número {nu1}...')
print(f'a unidade é {u}')
print(f'a dezena é {d}')
print(f'a centena é {c}')
print(f'o milhar é {m}')
