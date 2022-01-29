cont = soma = maior = menor = 0
resp = ' '
while resp != 'n':
    n = int(input('Digite um número'))
    resp = str(input('deseja continuar: [s/n]')).strip().lower()[0]
    if cont == 0:
        menor = n
        maior = n
    if n >= maior:
        maior = n
    if n <= menor:
        menor = n
    cont += 1
    soma += n
media = soma/cont
print('Foram digitados {} números, a média foi {}, o maior número foi {} e o menor {}'.format(cont, media,maior,menor))

