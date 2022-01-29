def perfeito():
    n = int(input('digite um número inteiro:'))
    while n <= 0:
        n = int(input('Você digitou um número inválido! Digite novamente, um número válido:'))
    for d in range(2, n+1):
        somadiv = 0
        for c in range(1, d):
            if d % c == 0:
                somadiv += c
        if d == somadiv:
            print(f'O número {d} é um número perfeito.')
        else:
            print(f'O número {d} não é um número perfeito.')


perfeito()
