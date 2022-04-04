print('===== DESAFIO 013 =====')
nome = input('olá funcionário! informe-nos o seu nome: ')
salario = float(input('digite seu salário: '))
porc = 15/100
calc1 = salario*porc
total = salario+calc1
print(f'{nome}, parabéns por seu desconto de 25%!')
print(f'seu salário era de {salario:.2f}, agora você passou a receber {total:.2f}. Parabéns!')