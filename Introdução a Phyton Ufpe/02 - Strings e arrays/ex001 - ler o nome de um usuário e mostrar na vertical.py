#QUESTÃO 01: Ler o nome do usuário e mostrar na vertical
nome = str(input('Digite seu nome:')).strip()

for c in range(0, len(nome)):
    print(f'{nome[c]}')