#calculo da média a partir de 3 números reais.
n1 = float(input('Digite a primeira nota:'))
while n1 < 0:
    n1 = float(input('Você digitou uma média negativa! Digite  novamente a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
while n2 < 0:
    n2 = float(input('Você digitou uma média negativa! Digite  novamente a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
while n3 < 0:
    n3 = float(input('Você digitou uma média negativa! Digite  novamente a terceira nota:'))
media = (n1+n2+n3)/3
print(f'Suas notas foram respectivamente:{n1,n2,n3} e sua média foi {media:.2f}')

