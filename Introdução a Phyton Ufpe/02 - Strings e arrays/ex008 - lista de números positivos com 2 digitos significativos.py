#QUESTÃO 08: lista de números positivos ocm 2 digitos significativos
n = 0
maior = []
maiorinver =[]
while n >= 0:
    n = int(input('digite um número inteiro: [Para parar digite um número negativo]'))
    if n > 9 and n < 100:
        maior.append(n)
maiorinver = maior[::-1]
print(f'Os números digitados com 2 dígitos significativos foram: {maiorinver}')