def contador(a,b,c):
    if c == 0:
        c = 1
    elif c < 0:
        c = c*-1
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    while b > a:
        print(f'{a}', end=' ')
        a += c
    b = b - c
    while a > b:
        print(f'{a}', end=' ')
        a -= c


print('='*30)
print(f'Contagem de 1 até 10 de 1 em 1:')
for con in range(1,11):
    print(con, end= ' ')
print('FIM')
print('='*30)
print(f'Contagem de 10 até 0 de 2 em 2:')
for dimi in range(10,-1, -2):
    print(dimi, end= ' ')
print('FIM')
print('='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
print('='*30)
contador(inicio, fim, passo)
print('FIM')