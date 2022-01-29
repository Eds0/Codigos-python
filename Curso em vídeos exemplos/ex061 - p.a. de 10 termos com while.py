a1 = int(input('digite o primeiro termo da p.a:'))
r = int(input('digite a razão da pa:'))
cont = 0
pa = a1
while not cont == 10:
    print(pa,end='-')
    pa += r
    cont+= 1