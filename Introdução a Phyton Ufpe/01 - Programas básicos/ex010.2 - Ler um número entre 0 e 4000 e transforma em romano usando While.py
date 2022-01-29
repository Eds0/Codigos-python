# QUESTÃO 10: Ler um número inteiro positivo N digitado pelo usuário e depois ler N números
# inteiros positivos (0 < x < 4000) e, para cada um deles, imprimir a sua
# representação em algarismos romanos.
n = int(input('Digite um número inteiro entre [0 e 4000]:'))
cont = 0
while n < 0 or n > 4000:
    n = int(input('Digite um número inteiro entre [0 e 4000]:'))
while cont < n:
    cont += 1
    uni = cont // 1 % 10
    dez = cont // 10 % 10
    cen = cont // 100 % 10
    mil = cont // 1000 % 10
    if uni != 0:
        if uni == 9:
            uni = str('IX')
        if uni == 8:
            uni = str('VIII')
        if uni == 7:
            uni = str('VII')
        if uni == 6:
            uni = str('VI')
        if uni == 5:
            uni = str('V')
        if uni == 4:
            uni = str('IV')
        if uni == 3:
            uni = str('III')
        if uni == 2:
            uni = str('II')
        if uni == 1:
            uni = str('I')
    elif uni == 0:
        uni = str('')
    if dez != 0:
        if dez == 9:
            dez = str('XC')
        if dez == 8:
            dez = str('LXXX')
        if dez == 7:
            dez = str('LXX')
        if dez == 6:
            dez = str('LX')
        if dez == 5:
            dez = str('L')
        if dez == 4:
            dez = str('XL')
        if dez == 3:
            dez = str('XXX')
        if dez == 2:
            dez = str('XX')
        if dez == 1:
            dez = str('X')
    elif dez == 0:
        dez = str('')
    if cen != 0:
        if cen == 9:
            cen = str('CM')
        if cen == 8:
            cen = str('DCCC')
        if cen == 7:
            cen = str('DCC')
        if cen == 6:
            cen = str('DC')
        if cen == 5:
            cen = str('D')
        if cen == 4:
            cen = str('CD')
        if cen == 3:
            cen = str('CCC')
        if cen == 2:
            cen = str('CC')
        if cen == 1:
            cen = str('C')
    elif cen == 0:
        cen = str('')
    if mil != 0:
        if mil == 1:
            mil = str('M')
        if mil == 2:
            mil = str('MM')
        if mil == 3:
            mil = str('MMM')
        if mil == 4:
            mil = str('MMMM')
    if mil == 0:
        if cen == 0:
            if dez == 0:
                print(uni)
            else:
                if uni == 0:
                    print(f'O número {cont} em romano é:{dez}')
                else:
                    print(f'O número {cont} em romano é:{dez}{uni}')
        else:
            if uni == 0 and dez == 0:
                print(f'O número {cont} em romano é:{cen}')
            else:
                print(f'O número {cont} em romano é:{cen}{dez}{uni}')
    else:
        if cen == 0 and dez == 0 and uni == 0:
            print(f'O número {cont} em romano é:{mil}')
        else:
            print(f'O número {cont} em romano é:{dez}{cen}{dez}{uni}')
