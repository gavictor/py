print('===== Desafio 004 =====')
print('Qual o tipo primitivo?')
inf1 = input('Digite algo: ')
print(f'O tipo primitivo deste dado é: ',type(inf1))
coleta1 = inf1.isnumeric()
coleta2 = inf1.isalpha()
coleta3 = inf1.isalnum()
coleta4 = inf1.isupper()
coleta5 = inf1.islower()
print(f'O dado digitado é númerico? {coleta1}')
print(f'O dado digitado é alfabetico? {coleta2}')
print(f'O dado digitado é alfanumerico? {coleta3}')
print(f'O dado digitado está somente em MAIUSCULAS? {coleta4}')
print(f'O dado digitado está somente em minusculas? {coleta5}')