def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'\033[31m ERRO: Por favor, digite um número inteiro válido \033[m')
            continue
        else:
            return numero


def leia_float(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31m ERRO: Por favor, digite um número real válido \033[m')
            continue
        else:
            return numero
