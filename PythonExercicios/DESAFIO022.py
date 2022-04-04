nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
nome2 = nome.split()
print(f'seu nome ao todo tem: {len(nome) - nome.count(" ")} letras')

#print(f"o primeiro nome tem {nome.find(' ')}")
separa = nome.split()
print(f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')