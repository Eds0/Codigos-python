#QUESTÃO 12: Calcular a média aritmética de vários números reais fornecidos pelo usuário. A
#leitura dos números deve parar quando um número negativo for lido.
n = float(input('Digite a sua 1° nota:'))
cont = soma = 0
media = n
while n > 0:
    cont += 1
    soma += n
    media = soma / cont
    n = float(input(f'Digite a sua {cont + 1}° nota:'))
print(f'A sua média foi: {media}')