def buscadordepalindromo():
    listapalindromo = []
    for c in range(100, 5001):
        n = str(c)
        ninverso = ''
        for c in range(len(n) - 1, -1, -1):
            ninverso += n[c]
        if ninverso == n:
            listapalindromo.append(ninverso)
    print(f'Existem {len(listapalindromo)} palindromos entre 100 e 5000!')
    print(f'Os palindromos são: {listapalindromo}\n')


def palindromo():
    n = int(input('Digite um número inteiro'))
    while n < 0:
        n = int(input('Você digitou um número inválido! Digite um número inteiro:'))
    n1 = str(n)
    ninverso = ''
    for c in range(len(n1)-1, -1, -1):
        ninverso += n1[c]
    if ninverso != n1:
        print('Não é um palindromo')
    else:
        print('É um palindromo')
    return print(f'O inverso de {n} é {ninverso}')


buscadordepalindromo()
palindromo()
