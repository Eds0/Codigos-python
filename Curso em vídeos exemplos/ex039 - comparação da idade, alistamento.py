ano = int(input('Digite o seu ano de nascimento:'))
idade = 2021 - ano
print('Sua idade é {}.'.format(idade))
if idade < 18:
    prazo = 18 - idade
    print('Você ainda irá se alistar! Faltam {} anos para você poder se alistar'.format(prazo))
elif idade == 18:
    print('Você está na hora de se alistar!')
else:
    prazo = idade - 18
    print('Você não precisa se alistar, você já passou {} anos do tempo de se alistar.'.format(prazo))
