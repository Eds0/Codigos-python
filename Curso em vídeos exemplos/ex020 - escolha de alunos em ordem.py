import random
n1 = str(input('Escreva o nome do primeiro aluno:'))
n2 = str(input('Escreva o nome do segundo aluno:'))
n3 = str(input('Escreva o nome do terceiro aluno:'))
n4 = str(input('Escreva o nome do quarto aluno:'))
alunos = [n1,n2,n3,n4]
random.shuffle(alunos)
print('Dos alunos {}, {}, {} e {} a sequência será {}'.format(n1,n2,n3,n4,alunos))