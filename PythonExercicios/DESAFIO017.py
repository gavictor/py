'''faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa'''
from math import hypot 
catetoOposto = float(input('Informe o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Informa o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'a hipotenusa vai medir {hipotenusa:.2f}')

'''
catetoOposto = float(input('Informe o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Informe o comprimento do cateto adjacente: '))
hi = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f'a hipotenusa vai medir {hi:.2f}')
'''