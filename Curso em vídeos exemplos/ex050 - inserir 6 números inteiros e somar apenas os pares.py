soma = 0
cont = 0
vezes = int(input('Digite quantos números você quer inserir?'))
for c in range(0,vezes):
    n = int(input('Digite um número:'))
    if n%2 == 0:
        soma += n
        cont += 1
print('Você digitou {} números e deles {} foram pares e  soma dos números pares foi {}'.format(vezes,cont,soma))
