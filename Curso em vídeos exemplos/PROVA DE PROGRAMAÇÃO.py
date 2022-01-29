from time import sleep
pos = []
neg = []
zer = []
for c in range(0,10):
    n = int(input(f'Digite o {c+1}° número:'))
    if n > 0:
       pos.append(n)
    elif n == 0:
        zer.append(n)
    else:
        neg.append(n)
sleep(0.5)
print('Estamos computando os números')
sleep(0.5)
print(f'Você digitou {len(pos)} números positivos e eles são: {pos} ')
print(f'Você digitou {len(neg)} números positivos e eles são: {neg} ')
print(f'Você digitou {len(zer)} números positivos e eles são: {zer} ')
