frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
reverso = ''
print('Vamos ver se é palíndromo ou não!')
for letra in range(len(junto)-1,-1,-1):
	reverso += junto[letra]
if junto == reverso:
	print(f'{junto} e {reverso} é palíndromo')
else:
	print(f'{junto} e {reverso} não é palíndromo')