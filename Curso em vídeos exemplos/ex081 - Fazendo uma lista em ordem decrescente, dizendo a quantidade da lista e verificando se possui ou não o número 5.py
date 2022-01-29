lista = []
while True:
    n = int(input("Digite um número:"))
    lista.append(n)
    resp = str(input('Deseja continuar:[S/N]'))
    if resp not in 'Ss' :
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'A sequência em ordem decrescente foi: {lista}.')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
