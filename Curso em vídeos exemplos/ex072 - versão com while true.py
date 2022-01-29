n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', \
    'dez', 'onze','doze', 'treze','quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',\
    'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número inteiro entre 0 e 20'))
        if num >= 0 and num <= 20:
            print(f'Vodê digitou o número {n[num]}.')
            break
    resp = str(input('Deseja continuar? [sim/não]')).strip().lower()[0]
    if resp == 'n':
        break
print('O programa foi finalizado')
