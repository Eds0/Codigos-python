resp = 0
while resp != 5:
    n1 = int(input('Digite o 1° número:'))
    n2 = int(input('Digite o 2° número:'))
    print('''O que você deseja fazer
    [1] - somar os números
    [2] - multiplicar os números
    [3] - descobrir qual número é o maior
    [4] - digitar novos números
    [5] - sair do programa''')
    resp = int((input('Digite o número da sua escolha:')))
    if resp == 1:
        soma = n1 + n2
        print(' {} + {} = {}'.format(n1,n2,soma))
    elif resp == 2:
        mult = n1*n2
        print(' {}x{} = {}'.format(n1, n2, mult))
    elif resp == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1,n2))
        elif n2>n1:
            print('O {} é maior que {}'.format(n2,n1))
        else:
            print('Os números são iguais!')
print('O programa encerrou')