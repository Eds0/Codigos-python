a = (int(input('Digite um número')), int(input('Digite um número')),
     int(input('Digite um número')), int(input('Digite um número')))
cont9 = 0
for c in a:
    if c == 9:
        cont9 += 1
    if c == 3:
        print(f'o 3 apareceu na {a.index(3) + 1}° posição')
    if c%2 == 0:
        print(f'Os números pares foram {c}')
print(f'O número 9 apareceu {cont9} vezes.')
