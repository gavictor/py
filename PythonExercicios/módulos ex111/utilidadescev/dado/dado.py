def leiaDado(msg):
    """
    A função valida se o dado é númerico ou não.
    Argumentos:
        msg: a mensagem que quer que apareça no input

    <-- Gabriel Victor -->
    """
    válido = False
    while válido == False:
        valor = input(msg).replace(',', '.')
        if valor.isalpha() or valor.strip() == '':
            print(f'\033[31mERRO, o valor digitado não é númerico.\033[m')
        else:
            válido = True
            return float(valor)

        