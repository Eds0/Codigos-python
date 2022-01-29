from time import sleep
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
print('Sua comparação está sendo feita...')
sleep(2)
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}!'.format(n1,n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro valor {}!'.format(n2,n1))
else:
    print('Não existe valor maior, o primeiro {} é igual ao segundo {}!'.format(n1,n2))
print('A comparação está pronta!')