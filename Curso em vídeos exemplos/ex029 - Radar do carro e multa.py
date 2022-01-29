velo = int(input('Qual a velocidade do carro em km/h:'))
print('Sua velocidade está sendo calculada...')
print('Sua velocidade é {} km/h'.format(velo))
if velo <= 80:
    print('A velocidade do carro está dentro do permitido!')
else:
    multa = (velo - 80)*7
    print('Você está com a velocidade a cima do permitido!')
    print('Você será multado em: {} R$'.format(multa))

