#QUESTÃO 06: Calcular o valor da série com N termos utilizando while.
numerador = denominador = 1
soma = cont = 0
n = int(input('Digite a quantidade de termos da série:'))
if n < 0:
    n *= -1
    print(f'Foi digitado um número negativo e será considerado o seu oposto {n}')
while cont < n:
   cont += 1
   if cont == 1:
    soma += numerador/denominador
   else:
       numerador += 2
       denominador += 1
       soma += numerador/denominador
print(f'A soma da série foi: {soma:.4f}')
