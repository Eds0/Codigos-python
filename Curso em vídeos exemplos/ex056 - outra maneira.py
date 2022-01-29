media = 0
m20 = 0
mvelho = 0
mnome = ''
for cont in range(1,5):
    print('--- {}° ---'.format(cont))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]')).strip().upper()
    media += idade
    if sexo == 'F' and idade < 20:
            m20 += 1
    else:
        if idade > mvelho:
            mvelho = idade
            mnome = nome
media = media/4
print('--' * 10)
print('A idade media foi {}'.format(media))
print('O homem mais velho foi {} com {} anos'.format(mnome, mvelho))
print('Existem {} mulheres abaixo de 20 anos'.format(m20))