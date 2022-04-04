print('===== DESAFIO 012 =====')
print('veremos o novo preço de seu produto!')
produto1 = float(input('digite o valor de seu produto: R$'))
sub = produto1 * 5 / 100
total = produto1-sub
print(f'O valor de seu produto era {produto1:.2f}, porem, em seu novo valor com 5% de desconto, ficará por {total:.2f}')