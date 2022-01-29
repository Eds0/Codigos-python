#QUESTÃO 02: ler o nome do usuário e mostrar na vertical
nome = str(input('Digite seu nome:')).strip()

for c in range(0, len(nome)+1):
    print(f'{nome[:c]}')
