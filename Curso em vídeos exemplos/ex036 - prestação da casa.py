print('- - '*7)
print('- - Financie sua casa - - -')
casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o valor do seu salário: R$'))
tempo = int(input('Em quantos anos você quer financiar:'))
parcela = casa/(tempo*12)
print('Sua parcela mensal ficou {:.2f} R$'.format(parcela))
if parcela >= 0.3*salario:
    print('Infelizmente você não poderá comprar a casa :/')
else:
    print('Seu cadastro foi aprovado! Você irá realizar seu sonho da casa própria.')

