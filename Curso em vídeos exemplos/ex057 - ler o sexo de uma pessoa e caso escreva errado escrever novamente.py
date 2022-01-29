res = ''
while not res == 'N':
    nome = str(input('Qual o seu nome?'))
    sexo = str(input('Qual o seu sexo [M]/[F]')).strip().upper()[0]
    while sexo not in 'MF':
        print('{} digitou um comando inválido'.format(nome))
        sexo = str(input('Qual o seu sexo [M]/[F]')).strip().upper()[0]
    res = str(input('Você quer continuar? [SIM/NÃO]')).strip().upper()[0]
print('Acabou')