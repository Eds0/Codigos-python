def numeros():
    n = int(input('Digite um número inteiro de até 5 digitos:'))
    while n > 99999:
        n = int(input('Erro você digitou um número com mais de 5 digitos! Digite um número inteiro de até 5 digitos:'))
    return n

def nbusca():
    nbusca = int(input('Digite um algarismo para ser buscado o algarismo [0 a 9]:'))
    while nbusca > 10 or nbusca < 0:
        nbusca = int(input('Erro você digitou um algarismo inválido! Digite um algarismo válido [0 a 9]:'))
    return nbusca


def lista5(c):
    digits = []
    unimil = c // 10000 % 10
    mil = c // 1000 % 10
    cen = c // 100 % 10
    dez = c // 10 % 10
    uni = c // 1 % 10
    if unimil == 0:
        if mil == 0:
            if cen == 0:
                if dez == 0:
                    digits.append(uni)
                else:
                    digits.append(dez)
                    digits.append(uni)
            else:
                digits.append(cen)
                digits.append(dez)
                digits.append(uni)
        else:
            digits.append(mil)
            digits.append(cen)
            digits.append(dez)
            digits.append(uni)
    else:
        digits.append(unimil)
        digits.append(mil)
        digits.append(cen)
        digits.append(dez)
        digits.append(uni)
    return digits


def busca(num, tam):
    contador = 0
    cont = lista5(tam)
    for c in range(len(cont)):
        if cont[c] == num:
            contador += 1
    return contador


def main():
    nlista = numeros()
    while nlista > 0:
        npesquisa = nbusca()
        print(f'Sua versão em lista é: {lista5(nlista)} e o algarismos 9 foi encontrado: {busca(9, nlista)}x')
        print(f'O algarismo {npesquisa} foi encontrado {busca(npesquisa, nlista)}x\n')
        nlista = numeros()
    if nlista <= 0:
        print('Fim do programa!')


main()
