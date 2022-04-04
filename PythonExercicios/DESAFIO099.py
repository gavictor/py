def maior(* num): # o asterisco informa que terão vários valores associados à função.
    cont = maior = 0
    print('\nAnalisando os valores passados.')
    for valores in num:
        cont += 1
        if cont == 0:
            cont = maior = valores
            print(f'O maior valor foi 0.')
        elif valores > maior:
            maior = valores
            
    print(f'O maior valor foi  {maior}, têm {cont} valores ao todo.')


# Programa Principal.

maior(2,4,5,7,9,1)

maior(4,7,0)
maior(1,2)
maior(6)
maior()
