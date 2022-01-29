#QUESTÃO 08: Construir uma tabela de conversão de graus Fahrenheit para Celsius, para todos os Fahrenheit While.
f1 = int(input('Digite a temperatura inicial'))
f2 = int(input('Digite a temperatura final'))
aux = f1
celsius = 0
if f1 > f2:
    f1 = f2
    f2 = aux
while f1 != f2:
    celsius = (f1 - 32) * 5 / 9
    f1 += 1
    print(f'As temperaturas em graus celsius entre o intervalo são {celsius:.2f}°')
