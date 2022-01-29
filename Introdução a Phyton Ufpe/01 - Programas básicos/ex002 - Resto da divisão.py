#QUESTÃO 02: Ler 2 números inteiros e calcular o resto da divisão
# do primeiro pelo segundo. Se o resto for zero, imprimir o primeiro número,
# senão imprimir o quadrado do resto.
n1 = int(input('Digite o primeiro número inteiro:'))
n2 = int(input('Digite o segundo número inteiro:'))
while n2 == 0:
    n2 = int(input('O segundo número não pode ser zero digite novamente!'))
divisao = n1%n2
if n1 >= n2:
    if divisao == 0:
        print(f'O primeiro número digitado foi {n1}')
    else:
        quadrado = pow(divisao, 2)
        print(f'O quadrado do resto da divisão é {quadrado}')
else:
    print(f'Não será possível realizar a divisão já que {n1} é menor que {n2}')
