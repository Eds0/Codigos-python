# S = 2/500 - 5/490 + 2/480 - 5/470
def serie(n, nu=2, de=500.0):
    if n <= 1:
        res = nu/de
        print(f'O {n}°termo é: {nu}/{de}')
    else:
        if nu == 2:
            res = nu/de + serie(n - 1, -5, de-10)
            print(f'O {n}°termo é: {nu}/{de}')
        else:
            res = nu/de + serie(n - 1, 2, de-10)
            print(f'O {n}°termo é: {nu}/{de}')
    return res


n = int(input('Digite a quantidade de termos da série:'))
while n < 0 or n > 50:
    n = int(input('Você digitou um número inválido, digite um novo número inteiro:'))

print(serie(n))


