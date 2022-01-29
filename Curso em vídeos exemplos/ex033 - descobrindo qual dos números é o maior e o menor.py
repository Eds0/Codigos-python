n1 = int(input('Escolha o primeiro número:'))
n2 = int(input('Escolha o segundo número:'))
n3 = int(input('Escolha o terceiro número:'))
if (n1>=n2) and (n1>=n3):
    if (n2>=n3):
        print('O maior número é {}.'.format(n1))
        print('O menor número é {}.'.format(n3))
    else:
        print('O maior número é {}.'.format(n1))
        print('O menor número é {}.'.format(n2))
else:
    if (n2>=n1) and (n2>=n3):
        if (n1 >= n3):
            print('O maior número é {}.'.format(n2))
            print('O menor número é {}.'.format(n3))
        else:
            print('O maior número é {}.'.format(n2))
            print('O menor número é {}.'.format(n1))
    else:
        if (n1 >= n2):
            print('O maior número é {}.'.format(n3))
            print('O menor número é {}.'.format(n2))
        else:
            print('O maior número é {}.'.format(n3))
            print('O menor número é {}.'.format(n1))
