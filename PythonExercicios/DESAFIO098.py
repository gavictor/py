#  de 1 até 10, de 1 em 1
#  de 10 até 0, de 2 em 2
#  uma contagem personalizada, o que o usuário decidir.
import getpass
usuario = getpass.getuser()
from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1 

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.6)
            cont += p
        print(f'{"Fim."}')
    else:
        cont=i
        while cont >= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.6)
            cont -= p
        print(f'Fim.')


contador(1,10,1)
contador(10,0,2)

print(f'Agora é a sua vez, {usuario}!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
