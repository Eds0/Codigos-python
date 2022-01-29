#QUESTÃO 04: ler o nome completo e mostrar o primeiro e o último nome.
nome = str(input('Digite seu nome completo')).strip().split()
print(f'Seu primeiro nome é: {nome[0].upper()}')
print(f'Seu último nome é: {nome[len(nome)-1].upper()}')