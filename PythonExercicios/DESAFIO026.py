frase =  str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {frase.count("a")} vezes na frase')
print(f'A letra A apareceu na posição {frase.find("a")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("a")+1}')