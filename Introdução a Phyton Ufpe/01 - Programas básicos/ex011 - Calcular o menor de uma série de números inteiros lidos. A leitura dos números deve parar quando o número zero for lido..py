#QUESTÃO 11: Calcular o menor de uma série de números inteiros lidos. A leitura dos números
# deve parar quando o número zero for lido.
n = int(input('Digite um número inteiro'))
menor = n
while n != 0:
    if n <= menor:
        menor = n
    n = int(input('Digite um número inteiro: [ou digite 0 para parar]'))
print(f'O menor número digitado foi {menor}!')