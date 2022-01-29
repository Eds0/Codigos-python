#QUESTÃO 09 - lista de um número positivo com 2 digitos
n = 0
cont = 0
maior = []
maiorinver =[]
while n >= 0 and cont <1000:
    n = int(input('digite um número inteiro: [Para parar digite um número negativo]'))
    if n > 9 and n < 100:
        maior.append(n)
    cont += 1
maiorinver = maior[::-1]
print(f'Os números digitados com 2 dígitos significativos foram: {maiorinver}')