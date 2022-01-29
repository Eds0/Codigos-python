def area(a,b):
    area = a*b
    print(f'A área do seu terreno {a}x{b} é de {area}m²')


print('-'*30)
print('Controle de Terreno')
a = float(input('Digite o comprimento(m):'))
b = float(input('Digite a largura(m):'))
area(a,b)
