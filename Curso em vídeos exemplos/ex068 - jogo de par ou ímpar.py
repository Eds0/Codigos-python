from random import randint
cont = 0
while True:
    jogada = str(input('Escolha se você quer [impar] ou [par]')).strip().lower()[0]
    jogador = int(input('Digite um número de 0 a 10:'))
    computador = randint(0,10)
    jogo = jogador + computador
    print(f'Você escolheu {jogador} e o computador escolheu {computador} e a soma deu {jogo}',end =' ')
    if jogada == 'i':
        if jogo%2 == 1:
            print('PARABÉNS, VOCÊ GANHOU!')
        else:
            break
    else:
        if jogo%2 == 0:
            print('PARABÉNS, VOCÊ GANHOU!')
        else:
            break
    cont+=1
print(f'Você PERDEU, o jogo foi encerrado! Você ganhou {cont} partidas')
