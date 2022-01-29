import time
numero =int(input('Digite um número INTEIRO:'))
base = str(input('Qual a base você quer converter?\n binário - [1] \n octal - [2]\n hexadecimal - [3]\n'))
print('O sistema está trabalhando...')
time.sleep(1)
if base == '1':
    print('O número {} na base binária fica {}'.format(numero,bin(numero)[2:]))
elif base == '2':
    print('O número {} na base octal fica {}'.format(numero,oct(numero)[2:]))
elif base == '3':
    print('O número {} na base hexadecimal fica {}'.format((numero),hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente!')
