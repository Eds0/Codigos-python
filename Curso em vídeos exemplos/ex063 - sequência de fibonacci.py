a1 = 0
a2 = 1
cont = 2
fim = int(input('Quantos termos você quer mostrar'))
print(a1, end=' ')
print(a2, end=' ')
while not cont >= fim:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    cont+= 1
    print(a3, end=' ')


