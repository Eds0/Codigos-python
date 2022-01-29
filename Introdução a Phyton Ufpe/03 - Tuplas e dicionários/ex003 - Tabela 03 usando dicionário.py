#QUESTÃO 03 COM DICIONÁRIO
soma = contalunos = cont = media = linferior = lsuperior = 0
tab = {} #criação do dicionário

cpf = int(input('Digite o cpf:'))
while cpf < 0:
    cpf = int(input('O código pessoal deve ser inteiro e positivo. Tente novamente: '))

while cpf > 0 and contalunos < 200:
    nome = input(f'Digite o nome referente a o código: {cpf}:')
    idade = int(input(f'Digite a idade de {nome}:'))
    tab[contalunos] = cpf, nome, idade
    cpf = int(input('\nDigite o cpf:'))
    contalunos += 1
print(f'\nForam digitados {contalunos} alunos e seus dados são:')
print(tab)

n = int(input('Digite a quantidade de intervalos que você deseja! '))
while n < 1:
    n = int(input('ERROR! Digite um valor de N [que seja positivo]:  '))

for i in range(n):
    linferior = int(input('Digite um intervalo inferior! '))
    lsuperior = int(input('Digite um intervalo superior! '))
    for i in range(n):
        nome, idade = tab[i][1:]
        if (idade >= linferior) and (idade <= lsuperior):
            print(f'Os alunos que se encaixam ndentro dos limites são:{tab[i]}')
        else:
            print(f'Não possui nenhum  aluno que se encaixe no limite: {linferior}:{lsuperior}')
    if linferior >= lsuperior:
        print('O limite inferior não pode ser maior que o superior.!\n')
        continue