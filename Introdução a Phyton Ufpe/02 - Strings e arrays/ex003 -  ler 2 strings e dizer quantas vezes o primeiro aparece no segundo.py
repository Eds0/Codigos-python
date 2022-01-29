#QUESTÃO 03: ler 2 strings e verificar quantas vezes a 1° está dentro da 2°
nome1 = str(input('Digite um nome:')).strip()
nome2 = str(input('Digite um nome:')).strip()
cont1 = cont2 = 0
saida = nome1 in nome2
if saida == True:
    while cont1 < len(nome2):
        if nome2[cont1:len(nome1) + cont1] == nome1:
            cont2 += 1
        cont1 += 1
    print(f'A string 1:"{nome1}" apareceu {cont2}x dentro da string 2:"{nome2}"')
else:
    print('A primeira string não está dentro da segunda string!')
