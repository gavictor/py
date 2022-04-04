'''há o preço de um produto, se pagar a vista, 10% de desconto, se parcelado, 8% de aumento!'''
preço = float(input('Digite o valor de seu produto de interesse: R$'))
print('À vista terá 10% de desconto, se à prazo, 8% de aumento!')
aVista = preço - (preço * 10 / 100)
aPrazo = preço + (preço * 8 / 100)
print(f'o valor de seu produto à vista, fica por {aVista:.2f}R$')
print(f'o valor de seu produto à prazo, fica por {aPrazo:.2f}R$')