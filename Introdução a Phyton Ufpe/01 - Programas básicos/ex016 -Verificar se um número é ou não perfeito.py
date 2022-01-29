#QUESTÃO16: Ler um número inteiro positivo e dizer se ele é perfeito ou não
n = int(input('digite um número inteiro:'))
while n <= 0:
    n = int(input('Você digitou um número inválido! Digite novamente, um número válido:'))
somadiv = 0
for c in range(1, n):
    if n%c == 0:
        somadiv += c
if n == somadiv:
    print(f'O número {n} é um número perfeito.')
else:
    print(f'O número {n} não é um número perfeito.')