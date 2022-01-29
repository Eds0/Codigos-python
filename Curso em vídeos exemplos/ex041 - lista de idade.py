anonas = int(input('Em qual ano você nasceu?'))
idade = 2021 - anonas
print('Sua idade é {} !'.format(idade))
if idade <= 9:
    print('Você concorrerá na categoria MIRIM')
elif (idade>9) and (idade<=14):
    print('Você concorrerá na categoria INFANTIL')
elif (idade>14) and (idade<=19):
    print('Você concorrerá na categoria JUNIOR')
elif(idade == 25):
    print('Você concorrerá na categoria SÊNIOR')
elif (idade>25):
    print('Você concorrerá na categoria MASTER')
