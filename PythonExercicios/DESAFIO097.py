while True:
    def escreva(msg):
        tam = len(msg) + 4
        print('~'* tam)
        print(f'  {msg}')
        print('~'* tam)


    mensagem = str(input('Seu texto: '))
    escreva(mensagem)

    while True:
        resposta = str(input('Continuar?[S/N]: '))[0].strip().upper()
        if resposta in 'SN':
            break
        print('Resposta Inválida.')
    if resposta  in 'N':
        break
escreva('Fim.')
