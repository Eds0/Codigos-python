sal = float(input('Qual o seu salário em R$:'))
print('Estamos calculando o seu aumento...')
print('Seu antigo salário era {:.2f} R$'.format(sal))
if (sal>1250):
    sal = sal*1.10
else:
    sal = sal*1.15
print('Seu novo salário é {:.2f} R$'.format(sal))