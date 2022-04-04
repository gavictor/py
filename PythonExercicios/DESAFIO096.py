def área(a,b):
    terreno = a * b
    print(f'A área do terreno com largura de {a} e comprimento de {b} é de {terreno:.2f}m²')


# programa principal
largura = float(input('Largura(M): '))
comprimento = float(input('Comprimento(M): '))
área(largura,comprimento)