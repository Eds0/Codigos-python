cont = -1
soma = num = 0
while num <998:
    num = int(input('Digite um número [999 para parar]:'))
    cont += 1
    soma += num
    if num >= 999:
        soma -= num
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
