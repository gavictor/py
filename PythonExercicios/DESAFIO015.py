'''escrever um programa que pergunte a quantidade de KM percorridos por um carro alugado e  a quantidade de dias pelos  quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
carro = int(input('Por quantos dias alugou o carro? '))
km = float(input('Quantos KMs rodou? '))
dia = 60.00 * carro
rodado = 0.15 * km
preço = dia + rodado
print(f'O valor total a se pagar são {preço:.2f}R$, sendo {dia:.2f}R$ por dias e {rodado:.2f}R$ por cada KM percorrido') 