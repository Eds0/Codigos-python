# S = 37*38/1 + 36*37/2 + 35*36/3
def serie(n, aux=37, nu=38, de=1.0):
    if n <= 1:
        res = ((aux*nu)/de)
        print(f'O {n}°termo é:{aux}*{nu}/{de}')
    else:
        res = ((aux*nu)/de) + serie(n - 1, aux-1, nu-1, de+1)
        print(f'O {n}°termo é:{aux}*{nu}/{de}')
    return res


n = int(input('Digite a quantidade de termos da série:'))
while n < 0:
    n = int(input('Você digitou um número inválido para esta série, digite um novo número inteiro:'))

print(serie(n))