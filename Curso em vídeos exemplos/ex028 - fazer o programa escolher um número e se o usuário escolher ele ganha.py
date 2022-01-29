import random
n = random.randint(0,5)
n1= int(input('Escolha um número:'))
if n == n1:
    print('O número gerado pelo {} e o escolhido foi {}. VOCÊ GANHOU!'.format(n,n1))
else:
    print('O número gerado pelo foi {} e o escolhido foi {}. VOCÊ PERDEU!'.format(n,n1))
