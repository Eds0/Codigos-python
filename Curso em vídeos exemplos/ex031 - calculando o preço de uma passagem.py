n = float(input('Qual a distância a ser percorrida na sua viagem em km:'))
print('O valor da sua passagem está sendo calculado...')
if (n<=200):
    passagem = n*0.5
else:
    passagem = n*0.45
print('O preço da sua passagem é {:.2f} R$'.format(passagem))

