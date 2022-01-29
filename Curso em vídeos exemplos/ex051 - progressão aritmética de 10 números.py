a1 = int(input('Digite o primeiro termo da P.A.'))
r = int(input('Digite a razão da P.A.'))
for c in range(0,10):
    print(a1,end='->')
    a1 += r
print('Fim da sequência dos 10 primeiros termos')
