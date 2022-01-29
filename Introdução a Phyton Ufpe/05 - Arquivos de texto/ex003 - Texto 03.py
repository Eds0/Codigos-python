def preencheTab():
    tabela = {}
    erroArq = True
    nomeArq = input('Nome do Arquivo: ')
    while erroArq:
        try:
            arqProf = open(nomeArq, 'r')
            erroArq = False
        except:
            print('Erro no arquivo, tente novamente')
            nomeArq = input('Nome do Arquivo: ')
    for prof in arqProf:
        codP = int(prof[:3])
        nomeP = prof[4:29]
        areaP = prof[30:40]
        tabela[codP] = (nomeP, areaP)
    arqProf.close()
    return tabela


try:
    tab = preencheTab()
    print(f'Tabela com {len(tab)} profissões foi lida corretamente.')
    print('Tabela ->', tab)
    saida = open('profissao.inexistente.text', 'w')
    codP = int(input('Digite um código de profissão para busca [<=0 para parar]: '))
    while codP > 0:
        if codP in tab:
            nomeP, areaP = tab[codP]
            print(f'Profissão {codP} é {nomeP} e sua área é {areaP}.')
        else:
            print(f'Profissão {codP} não existe na tabela.')
            saida.write(f'{codP}\n')
        codP = int(input('Digite outro código para busca [<=0 para parar]: '))
    saida.close()
except:
    print('Houve erro no programa')

print('Fim de Programa')

