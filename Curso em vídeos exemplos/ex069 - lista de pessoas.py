m18 = home = m20 = 0
while True:
    print('--- CADASTRANDO UMA PESSOA ---')
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('------------------------------')
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        home += 1
    if sexo == 'F' and idade > 20:
        m20 +=1
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {m18} maiores de 18 anos,  {home} homens e {m20} mulheres maiores do que 20 anos.')

