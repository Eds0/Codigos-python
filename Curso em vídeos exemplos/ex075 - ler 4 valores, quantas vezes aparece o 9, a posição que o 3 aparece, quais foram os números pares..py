a = (int(input('Digite um número')), int(input('Digite um número')),
     int(input('Digite um número')), int(input('Digite um número')))
print(f'O número 9 apareceu {a.count(9)} vezes.')
if 3 in a:
    print(f'O número 3 apareceu na {a.index(3)+1}° posição')
else:
    print('Não foi digitado nenhum 3')
print(f'Os números pares foram',end = ' ')
for c in a:
    if c%2 == 0:
        print(c,end = ',')
