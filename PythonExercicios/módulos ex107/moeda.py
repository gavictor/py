def aumentar(num, porc=0):
    """
    -> Essa função mostra o valor adicionado à porcentagem desejada
    :param num: o valor que vai ser adicionado
    :param porc: a porcentagem de aumento.
    :return: retorna o valor aumentado.
    """
    calc = num * (porc/100)
    num += calc
    return num 


def diminuir(num, porc=0):
    """
    -> Essa função mostra o valor reduzido à porcentagem desejada
    :param num: o valor que vai ser subtraído
    :param porc: a porcentagem de redução.
    :return: retorna o valor diminuído.
    """
    calc = num * (porc/100)
    num -= calc
    return num

def dobro(num):
    """
    -> Essa função mostra o dobro de um valor
    :param num: o valor que vai ser mostrado o dobro
    :return: retorna o dobro do valor
    """
    num *= 2
    return num

def metade(num):
    """
    -> Essa função mostra a metade de um valor
    :param num: o valor que vai ser mostrado a metade
    :return: retorna o valor pela metade
    """
    num /= 2
    return num

    