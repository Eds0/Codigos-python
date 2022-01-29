n = int(input('Qual número você quer que seja a tabuada'))
for c in range (1,11):
    mult = n*c
    print('{}x{}={}'.format(n,c,mult))
print('A TABUADA DE {} ESTÁ PRONTA!'.format(n))

