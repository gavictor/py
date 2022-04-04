import moeda
valor = int(input('Digite um valor: R$'))
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.aumentar(valor,10,True)}')
print(f'Diminuindo 13% de {moeda.moeda(valor)} temos {moeda.diminuir(valor,13,True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor,True)}')