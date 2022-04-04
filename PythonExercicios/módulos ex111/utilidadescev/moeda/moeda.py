def resumo(num, porcaum=0, porcdim=0):
	print(f'<------->'*2)
	print(f'Resumo do Valor'.center(18))
	print(f'<------->'*2)


	print(f'{"Preço analisado: ":<7} \t{moeda(num)}\n')
	print(f'{"Dobro do Preço: ":<7} \t{dobro(num,True)}')
	print(f'{"Metade do Preço: ":<7} \t{metade(num,True)}')
	print(f'{f"{porcaum}% de Aumento: ":<7} \t{aumentar(num, porcaum, True)}')
	print(f'{f"{porcdim}% de Redução: ":<7} \t{diminuir(num, porcdim, True)}')
	print(f'<------->'*2)



def aumentar(num, porc=0, show=False):
    """
    -> Essa função mostra o valor adicionado à porcentagem desejada
    :param num: o valor que vai ser adicionado
    :param porc: a porcentagem de aumento.
    :return: retorna o valor aumentado.
    """
    calc = num * (porc/100)
    num += calc
    if show:
        return f'{moeda(num)}'
    else:
        return num

def diminuir(num, porc=0, show=False):
    """
    -> Essa função mostra o valor reduzido à porcentagem desejada
    :param num: o valor que vai ser subtraído
    :param porc: a porcentagem de redução.
    :return: retorna o valor diminuído.
    """
    calc = num * (porc/100)
    num -= calc
    if show:
        return f'{moeda(num)}'
    else:
        return num

def dobro(num, show=False):
    """
    -> Essa função mostra o dobro de um valor
    :param num: o valor que vai ser mostrado o dobro
    :return: retorna o dobro do valor
    """
    num *= 2
    if show:
        return f'{moeda(num)}'
    else:
        return num
    

def metade(num, show=False):
    """
    -> Essa função mostra a metade de um valor
    :param num: o valor que vai ser mostrado a metade
    :return: retorna o valor pela metade
    """
    num /= 2
    if show:
        return f'{moeda(num)}'
    else:
        return num


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')
