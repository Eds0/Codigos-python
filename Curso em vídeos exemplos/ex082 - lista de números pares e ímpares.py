lista = []
par = []
impar = []
while True:
    n = int(input("Digite um número:"))
    lista.append(n)
    if n%2 == 1:
        impar.append(n)
    else:
        par.append(n)
    resp = str(input('Deseja continuar:[S/N]'))
    if resp not in 'Ss':
        break
print(f'A lista completa foi: {lista}')
print(f'A lista par é: {par}')
print(f'A lista ímpar é {impar}')
