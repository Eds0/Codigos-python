#tabela 01, cada curso código (número inteiro), (nome string) e o centro (inteiro positivo)
#tabela de cursos para com o código de cursos zero.
#QUESTÃO 01 COM DICIONÁRIO
tab = {} #criação do dicionário
codcurso = int(input('Digite o código do Curso:'))
while codcurso < 0:
    codcurso = int(input('O código do cursos deve ser inteiro e positivo. Tente novamente: '))
while codcurso != 0:
    nome = input(f'Digite o nome do curso {codcurso}:')
    codcentro = int(input(f'Digite o código do centro do curso {nome}:'))
    while codcentro < 1:
        codcentro = int(input('O código do cursos deve ser inteiro e positivo. Tente novamente:'))
    tab[codcurso] = (nome, codcentro)
    codcurso= int(input('Digite o código do Curso: ou [0] para parar'))
    while codcurso < 0:
        codcurso = int(input('O código do cursos deve ser inteiro e positivo. Tente novamente: '))
print(tab)
buscacodcentro = int(input('Digite um código do centro para busca: '))
while buscacodcentro < 1:
    buscacodcentro = int(input('Digite um código centro inteiro positivo para busca: '))
encontrou = False
while buscacodcentro > 0:
    for c in tab:  # verifica se a profissão existe na tabela
        nome, codcentro = tab[c]
        if buscacodcentro in tab[c]:
            print(f'O centro {codcentro} possui os seguintes cursos:')
            print(f'{nome} e o de código: {c}')
            encontrou = True
    if not encontrou:
        print(f'Nenhum curso encontrado para o centro {buscacodcentro}')
    buscacodcentro = int(input('Digite um novo código de busca de centro [ou um número não positivo para parar]: '))
print('Terminar processo.')
