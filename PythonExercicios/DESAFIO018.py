'''faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''
print('===== DESAFIO 018 =====')
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'o valor do seno de {angulo} é {seno:.2f}')
print(f'o valor do cosseno de {angulo} é {cosseno:.2f}')
print(f'o valor da tangente de {angulo} é {tangente:.2f}')