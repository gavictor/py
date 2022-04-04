print('===== DESAFIO 020 =====')
print('Sequência de alunos à apresentar o trabalho!')
from random import shuffle
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'A sequência de alunos a se apresentar é')
print(alunos)