print('------'*10)
print('-------- Testando se poderá ser feito um triângulo ---------')
l1 = float(input('Defina o primeiro lado do triângulo em cm:'))
l2 = float(input('Defina o segundo lado do triângulo em cm:'))
l3 = float(input('Defina o terceiro lado do triângulo em cm:'))
if l1<l2+l3 and l2<l1+l3 and l3< l1+l2:
    print('As condições foram atendidas e o triângulo poderá ser formado!')
else:
    print('As condições não foram atendidas escolha outros valores!')
print('------'*10)