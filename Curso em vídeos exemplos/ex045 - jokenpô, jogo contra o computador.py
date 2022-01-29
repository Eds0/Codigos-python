import random
import time
print('JOKENPÔ')
print('''
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
''')
jogador = int(input('Escolha a sua jogada'))
jogo = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)
print('JÔ')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
if jogador == 0: #pedra
    if computador == 1: #papel
        print('''DERROTA!!!!! O COMPUTADOR ESCOLHEU {}E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador],jogo[jogador]))
    elif computador ==2: #tesoura
        print('''VITÓRIA!!!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador], jogo[jogador]))
    else:
        print('O JOGO SAIU EMPATE!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador], jogo[jogador]))
elif jogador == 1: #papel
    if computador == 0: #pedra
        print('''VITÓRIA!!!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador],jogo[jogador]))
    elif computador ==2: #tesoura
        print('''DERROTA!!!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador], jogo[jogador]))
    else:
        print('O JOGO SAIU EMPATE!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador], jogo[jogador]))
else:
    if computador == 0: #pedra
        print('''DERROTA!!!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador],jogo[jogador]))
    elif computador ==1: #papel
        print('''VITÓRIA!!!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador], jogo[jogador]))
    else:
        print('O JOGO SAIU EMPATE!!! O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'''
        .format(jogo[computador], jogo[jogador]))
