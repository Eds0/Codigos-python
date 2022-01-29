while True:
    n = int(input('Quer ver a tabuada de qual número:'))
    if n < 0:
        break
    print('-' * 10)
    for c in range(1,11):
        print(f'{c}x{n}={c*n}')
    print('-' * 10)
print('Terminaram as tabuadas')

