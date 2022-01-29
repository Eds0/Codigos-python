n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', \
    'dez', 'onze','doze', 'treze','quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',\
    'dezenove', 'vinte')
num = int(input('Digite um número inteiro entre 0 e 20'))
while (num < 0):
    num = int(input('Digite um número inteiro entre 0 e 20'))
while (num > 20):
    num = int(input('Digite um número inteiro entre 0 e 20'))
print(f'Vodê digitou o número {n[num]}.')
