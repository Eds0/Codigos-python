menori = 0
for c in range(0,7):
    nome = str(input('Digite o seu nome:'))
    nasc = int(input('Digite o ano em que nasceu:'))
    idade = 2021 - nasc
    if idade <18:
        print('{} tem {} e ainda não atingiu a maioridade!'.format(nome,idade))
        menori += 1
    else:
        print('{} tem {} e já tem a maioridade!'.format(nome,idade))
maiori = 7 - menori
print('Tiveram {} pessoas maior de idade e {} menor idade.'.format(maiori,menori))
