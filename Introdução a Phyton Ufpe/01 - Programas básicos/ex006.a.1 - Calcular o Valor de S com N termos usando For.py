#QUESTÃO 06: Calcular o valor da série com N termos utilizando for.
numerador = denominador = 1
soma = 0
n = int(input('Digite a quantidade de termos da série:'))
if n < 0:
    n *= -1
    print(f'Foi digitado um número negativo e será considerado o seu oposto {n}')
for c in range(0, n):
   if c == 0:
    soma += numerador/denominador
   else:
       numerador += 2
       denominador += 1
       soma += numerador/denominador
print(f'A soma da série foi: {soma:.4f}')
