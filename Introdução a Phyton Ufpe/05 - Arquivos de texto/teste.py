def leitura():
    try:
        entradacentros = open('centros.arq.txt', 'r')
        entradadisciplina = open('discip.arq.txt', 'r')
        saidadisciplinacompleto = open('discipCompleto.arq.text', 'w')
        tabelacentro = {}
        contCentro = 0
        contDisciplina = 0
        for linha in entradacentros:
            codigocentro = linha[0:2]
            nomecentro = linha[3:28]
            tabelacentro[codigocentro] = nomecentro
            contCentro += 1
        for linha in entradadisciplina:
            codigodisciplina = linha[0:5]
            nomedisciplina = linha[6:41]
            creditosdisciplina = linha[42:44]
            codigocentrodisciplina = linha[45:47]
            nomecentrodisciplina = tabelacentro[codigocentrodisciplina]
            saidadisciplinacompleto.write(f'{codigodisciplina} {nomedisciplina} {creditosdisciplina} {codigocentrodisciplina} {nomecentrodisciplina}\n')
            contDisciplina += 1
        print(f'Existem {contDisciplina} disciplinas no arquivo {entradadisciplina} e {contCentro} centros no arquivo {entradacentros}.')
        entradacentros.close()
        entradadisciplina.close()
        saidadisciplinacompleto.close()
    except:
        print('Erro no função de leitura, revise-o!')

def findcenter():
    try:
        find = input('Insira o código a ser buscado: ')
        tabelafind = {}
        entradacentros = open('centros.arq.txt', 'r')
        for linha in entradacentros:
            codigocentro = linha[0:2]
            nomecentro = linha[3:28]
            tabelafind[codigocentro] = nomecentro
        entradacentros.close()
        if find in tabelafind:
            return tabelafind[find]
        else:
            return print(f'O código digitado não foi encontrado!')
    except:
        print('Erro na função de busca, revise-o!')

def main():
    try:
        leitura()
        findcenter()
    except:
        print('Erro na função principal, examine todo o script!')

try:
    main()
except:
    print('ERRO NO SCRIPT')