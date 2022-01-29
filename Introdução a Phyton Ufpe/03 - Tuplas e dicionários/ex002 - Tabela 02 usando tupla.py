#tabela 01, cada curso código (número inteiro), (nome string) e o centro (inteiro positivo)
#tabela de cursos para com o código de cursos zero.
#QUESTÃO 02 COM TUPLAS
soma = cont = media = 0
tab = [] #criação da tupla

codigointeiro = int(input('Digite o código pessoal:'))
while codigointeiro < 0:
    codigointeiro = int(input('O código pessoal deve ser inteiro e positivo. Tente novamente: '))

while codigointeiro > 0:
    nome = input(f'Digite o nome referente a o código: {codigointeiro}:')
    salario = float(input(f'Digite o salário de {nome}:'))
    while salario < 0:
        salario = int(input(f'O salário de {nome} deve ser inteiro e positivo. Tente novamente:'))
    tab.append([codigointeiro, nome, salario])
    codigointeiro = int(input('\nDigite o código pessoal:'))
print(tab)

salariomax = float(input('Digite o valor de salário máximo: '))
while salariomax < 1:
    salariomax = int(input('ERROR! Digite um valor de salário máximo válido [que seja positivo]:  '))

for i in range(len(tab)):
    if tab[i][2] <= salariomax:
        cont += 1
        soma += tab[i][2]
        print(f'{tab[i][1]} com código: {tab[i][0]} e salário: {tab[i][2]} teve um salário menor que {salariomax}')
if cont == 0:
    print(f'Nenhum salário é menor ou igual a {salariomax}')
media = soma/cont
print(f'\nTiveram {cont} pessoas com salários menores ou iguais a {salariomax} e a média de salário delas foi {media}')
