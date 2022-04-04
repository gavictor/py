print('===== Desafio 019 =====')
from random import choice
aluno1 = input('Primeiro  Aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido foi {choice(alunos)}')