# Considere um arquivo texto com nome externo 'discip.arq', contendo informações
# de disciplinas: código com 5 posições, nome com 35 posições, créditos com 2
# posições, e código do centro a que pertence com 2 posições; uma disciplina por
# linha.
# Considere também um outro arquivo texto com nome externo 'centros.arq',
# contendo informações de centros: código com 2 posições e nome com 25
# posições; também um centro por linha.

# Seu programa deve, usando um procedimento, (a) ler o arquivo de centros e
# colocar seu conteúdo em uma tabela
# e depois (b)
# gravar um arquivo texto de nome externo 'discipCompleto.arq',
#
#
# contendo todas as informações do arquivo
# 'discip.arq' e mais o nome do centro a que pertence.
#
# No final seu programa deve imprimir para o usuário a quantidade de disciplinas e de centros.
# OBS: Você deve escrever também uma função para achar o nome do centro a
# partir do seu código.

try:
    try:
        entradadisciplina = open('discip.arq.txt', 'r')
        entradacentros = open('centros.arq.txt', 'r')
        saidadisciplinacompleto = open('discipCompleto.arq.text', 'w')
    except:
        print('Erro de manipulação dos arquivos, tente novamente!')
        entradadisciplina = open('discip.arq.txt', 'r')
        entradacentros = open('centros.arq.txt', 'r')
        saidadisciplinacompleto = open('discipCompleto.arq.text', 'w')
    tabelacentro = []
    def main():
        contDisciplina = 0
        contCentro = 0
        for line in entradacentros:
            codigocredito = line[0:2]
            nomecredito = line[3:28]
            tabelacentro[codigocredito] = nomecredito
            contCentro += 1
        for line in entradadisciplina:
            codigodisciplina = line[0:5]
            nomeDisciplina = line[6:41]
            creditoDisciplina = line[42:44]
            codigoCentroDisciplina = line[45:47]
            nomecentroDisciplina = tabelacentro[codigoCentroDisciplina]
            saidadisciplinacompleto.write(f'{codigodisciplina} {nomeDisciplina} {creditoDisciplina}'
                                          f'{ codigoCentroDisciplina} {nomecentroDisciplina}\n')
            contDisciplina += 1
        entradacentros.close()
        entradadisciplina.close()
        saidadisciplinacompleto.close()
        return tabelacentro


    def buscacentro():
        buscacodigo = input('insira o código do centro:')
        if buscacodigo in main():
            return tabelacentro[buscacodigo]


    main()
    buscacentro()
    print(f' O código do centro é {buscacentro()}')

except:
    print('Erro no programa principal, revise o programa!')


    # for i in range(len(texto)):
    #     tabela.append(texto[i].split())
    # print(tabela)
    #
    # def buscacentro():
    #     for c in range(len(tabela)):
    #         if codigoCentro == tabela[c][0:2]:
    #             return[i][3:28]
    #     return False
    #
    # for line in entradadisciplina:
    #     codigo = line[0:5]
    #     nome = line[6:41]
    #     credito = line[42:44]
    #     codigoCentro = line[45:47]

