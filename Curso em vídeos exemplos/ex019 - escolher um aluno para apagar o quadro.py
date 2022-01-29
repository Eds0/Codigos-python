from random import choice
n1 = str(input('Escreva o nome do primeiro aluno:'))
n2 = str(input('Escreva o nome do segundo aluno:'))
n3 = str(input('Escreva o nome do terceiro aluno:'))
n4 = str(input('Escreva o nome do quarto aluno:'))
alunos = [n1,n2,n3,n4]
escolhido = choice(alunos)
print('Dos alunos {}, {}, {} e {} o escolhido foi {}'.format(n1,n2,n3,n4,escolhido))
