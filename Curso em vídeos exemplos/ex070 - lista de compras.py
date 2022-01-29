cont = soma = mil = menor = 0
mnome = ''
while True:
    prod = str(input('Qual o nome do produto:'))
    n = float(input('Quanto custa:'))
    resp = str(input('deseja continuar: [s/n]')).strip().lower()[0]
    if cont == 0:
        menor = n
    if n <= menor:
        menor = n
        mnome = prod
    if n > 1000:
        mil+=1
    cont += 1
    soma += n
    if resp == 'n':
        break
print(f'Foram digitados R${cont} produtos,a conta total deu R${soma}.')
print(f'O produto {mnome} foi o mais barato custando R${menor}.')
print(f'Tivemos {mil} acima de R$ 1000.')