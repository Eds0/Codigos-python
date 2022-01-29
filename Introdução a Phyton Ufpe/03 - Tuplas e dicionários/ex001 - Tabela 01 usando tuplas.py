#tabela 01, cada curso código (número inteiro), (nome string) e o centro (inteiro positivo)
#tabela de cursos para com o código de cursos zero.
#QUESTÃO 01 COM TUPLA
i = 0
tab = [] #criação da tupla

codcurso = int(input('Digite o código do curso:'))
while codcurso < 0:
    codcurso = int(input('O código do cursos deve ser inteiro e positivo. Tente novamente: '))

while codcurso != 0:
    nome = input(f'Digite o nome do curso de codigo {codcurso}:')
    codcentro = int(input(f'Digite o código do centro do curso {nome}:'))
    while codcentro < 1:
        codcentro = int(input('O código do cursos deve ser inteiro e positivo. Tente novamente:'))
    tab.append([codcurso, nome, codcentro])
    codcurso = int(input('Digite o código do curso:'))
    while codcurso < 0:
        codcurso = int(input('O código do cursos deve ser inteiro e positivo. Tente novamente: '))
print(tab)

buscacodcentro = int(input('Digite um código do centro para busca: '))
while buscacodcentro < 1:
    buscacodcentro = int(input('Digite um código centro inteiro positivo para busca: '))

while buscacodcentro > 0:
    for i in range(len(tab)):
        if buscacodcentro == tab[i][2]:  # Verifica se o centro existe na tabela
            print(tab[i])
        else:
            print(f'Nenhum curso encontrado para o centro {buscacodcentro}')
    buscacodcentro = int(input('Digite um novo código de busca de centro [ou um número não positivo para parar]: '))
print('Terminar processo.')
