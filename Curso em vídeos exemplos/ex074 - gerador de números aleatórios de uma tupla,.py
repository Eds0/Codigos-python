from random import randint
a = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores escolhidos foram:',end=' ' )
for c in a:
    print(c,end=' ')
print(f'\nO maior valor foi {max(a)}')
print(f'O menor valor foi {min(a)}')
