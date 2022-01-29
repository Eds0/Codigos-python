produto = float(input('Digite o preço do produto:'))
pagamento = str(input('Escolha a forma de pagamento: [a vista] ou [parcelado]')).strip().upper()
if pagamento == 'A VISTA':
    formato = int(input('Escolha o formato de pagamento: dinheiro [1], cheque [2] ou cartão [3].'))
    if formato == 3:
        produto = 0.95*produto
        print('O valor a ser pago será {} R$.'.format(produto))
    else:
        produto = 0.9*produto
        print('O valor a ser pago será {} R$.'.format(produto))
elif pagamento == 'PARCELADO':
    parcelamento = int(input('Digite quantas vezes você quer parcelar o seu produto?'))
    if parcelamento <= 2:
        print('O valor do produto será {} e sua parcela será {:.2f}'.format(produto, produto/parcelamento))
    else:
        produto = produto*1.2
        print('o valor do produto será {} e sua parcela será {:.2f}.'.format(produto, produto/parcelamento))
