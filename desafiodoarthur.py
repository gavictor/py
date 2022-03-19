import os
vida = 3
palavra = str(input('Digite uma palavra: '))
letras = ''
char = [len(palavra)]
for traços in char:
    print('-'*traços)
while True:
    escolha = str(input('Digite uma letra: '))[0].strip()
    for acertar in escolha:
        if escolha in palavra:
            letras += escolha
            print(f'Parabéns, a letra {escolha} está na palavra.')
        if escolha in letras:
            print('Essa letra já foi adicionada.')
            if letras == palavra:
                print('Você ganhou.')
                break
        elif escolha not in palavra:
            vida -= 1
            print(f'{escolha} não está na palavra, restam {vida} vidas.')
            if vida <= 0:
                break