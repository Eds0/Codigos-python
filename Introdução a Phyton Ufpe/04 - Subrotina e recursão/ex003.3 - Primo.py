def primo():
    n = int(input('digite um número inteiro:'))
    while n <= 0:
        n = int(input('Você digitou um número inválido! Digite novamente, um número válido:'))
    primo = 0
    for c in range(1, n+1):
        if n%c == 0:
            primo += 1
    if primo == 2:
        print(f'O número {n} é um número primo.')
    else:
        print(f'O número {n} não é um número primo.')


primo()
