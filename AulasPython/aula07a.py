"""
nome = input('Qual é seu nome? ')
print(f'prazer em te conhecer, {nome:=^20}!')
"""

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
sub = n1-n2
p = n1**n2
d = n1/n2
di = n1//n2
print(f'a soma vale {n1+n2} o produto vale {m} e a divisão vale {d:.3f}',end=' >>> ')
print(f'divisão inteira == {di} e potência == {p}')