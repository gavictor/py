import moeda
valor = int(input('Digite um valor: R$'))
print(f'Aumentando 10% de {valor} temos {moeda.aumentar(valor,10)}')
print(f'Diminuindo 13% de {valor} temos {moeda.diminuir(valor,13)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')