print('=====  Desafio 010 =====')
print('Veremos quantos doláres você pode comprar!')
us = 5.14
rs = float(input('Quantos reais você tem na carteira? R$'))
calc =  rs / us
euro = 0.17 * rs
print(f'com {rs}R$, você pode comprar até {calc:.2f}$')
print(f'com {rs}R$, você pode comprar até {euro:.2f} Euros')