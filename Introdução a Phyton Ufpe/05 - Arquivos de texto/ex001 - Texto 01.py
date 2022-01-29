# Testa arquivos texto básicos de entrada e saída

try:
    entrada = open('discip.old.text', 'r')
    saida = open('discip.new.text', 'w')
    contdisciplina = 0
    contcredito = 0
    contsaida = 0
    for line in entrada:
        codigo = line[0:5]
        nome = line[6:41]
        credito = line[42:44]
        cargahoraria = int(credito)*15
        contdisciplina += 1
        if codigo != 'IF125' and codigo != 'IF380':
            if codigo[0:2] == 'MA':
                credito = 5
                cargahoraria = int(credito) * 15
                contcredito += 1
            saida.write(f'{codigo} {nome} {credito} {cargahoraria:>4}\n')
            print(f'Número de codigo gravado = {codigo}{credito}')
    entrada.close()
    saida.close()
    contsaida = contdisciplina - contcredito
except:
    print('ERROR! Revise o programa')
