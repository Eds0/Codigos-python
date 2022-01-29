print('Tabela usando dicionário\n')

# tabela chave curso = {código, nome, centro}
# a consulta não é feita por chave

tab_cursos = {} #criação do dicionário

n = int(input('Digite o tamanho da tabela de cursos: '))
while n < 0:
    n = int(input('Digite novamente um inteiro positivo: '))

for i in range(n):  # o i é criado apenas para o for
    codigo = int(input(f'Digite o código do {i+1}º curso: '))
    while codigo < 0:
        codigo = int(input(f'Não é permitido digitar 0. Digite novamente o código do {i + 1}º curso: '))
    if codigo == 0:
        n = i + 1
    else:
        nome = input(f'Digite o nome do {i+1}º curso: ')
        centro = int(input(f'Digite o número do {i+1}º centro: '))
        tab_cursos[i] = (codigo, nome, centro)
        # tab_cursos[codigo] = (nome, centro)

    print(f'Tabela: {tab_cursos}')

busca = int(input('\nDigite um código do centro para busca: '))
while busca < 1:
    busca = int(input('\nDigite um código centro inteiro positivo para busca: '))
existe = False
while busca > 0:
    for chave in tab_cursos: # verifica se a profissão existe na tabela
        codigo, nome, centro = tab_cursos[chave]
        # for codigo in tab_cursos:
            # nome, centro = tab_cursos[codigo]
        print(codigo)
        print(busca)
        if centro == busca:
            print(f'O código {codigo} do curso tem nome {nome} e centro {centro}')
            existe = True
    if not existe:
        print('\nNão foi possível encontrar nenhum curso com centro informado.')
    busca = int(input('\nDigite um nov código de busca de centro (ou zero para parar): '))


print('Terminar processo.')