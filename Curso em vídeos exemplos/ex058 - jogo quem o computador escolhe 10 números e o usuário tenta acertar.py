#jogo para descobrir o número que o computador pensou
from random import randint
comp = randint(0,10)
cont = 1
jogador = int(input('Escolha um número inteiro'))
while jogador != comp:
    cont += 1
    if jogador > comp:
        print('Menos...')
    else:
        print('Mais...')
    jogador = int(input('Escolha um número inteiro'))
print('Você acertou na {}° tentativa'.format(cont))
