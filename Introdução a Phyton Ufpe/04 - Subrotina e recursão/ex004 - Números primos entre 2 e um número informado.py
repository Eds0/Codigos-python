def primo():
    n = int(input('digite um número inteiro:'))
    while n <= 0:
        n = int(input('Você digitou um número inválido! Digite novamente, um número válido:'))
    for b in range(n+1):
        primo = 0
        for c in range(1, b+1):
            if b%c == 0:
                primo += 1
        if primo == 2:
            print(f'O número {b} é um número primo.')


primo()
