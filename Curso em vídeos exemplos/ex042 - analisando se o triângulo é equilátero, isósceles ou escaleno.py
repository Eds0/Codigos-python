l1 = float(input('Digite o primeiro lado'))
l2 = float(input('Digite o segundo lado'))
l3 = float(input('Digite o terceiro lado'))
if l1 + l2> l3 and l1+ l3 > l2 and l2 + l3 > l1:
    print('Os 3 lados formam um triângulo!')
    triang = str('vdd')
    if l1 == l2 and l1 == l3:
        print('O triângulo formado é um triângulo EQUILÁTERO!')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triângulo formado é um triângulo ESCALENO!')
    else:
        print('O triângulo formado é um triângulo ISÓSCELES!')
else:
    print('Os 3 lados não formam um triângulo!')

