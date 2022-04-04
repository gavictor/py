from getpass import getuser
from utilidadescev.moeda import moeda
from utilidadescev.dado import dado

print(f'Olá, {getuser()} Tudo Bem?')
valor = dado.leiaDado('Digite o preço de seu produto: R$')
moeda.resumo(valor, 80, 35)