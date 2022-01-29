frase = str(input('Digite uma frase')).strip().lower().split()
palavras = ''.join(frase)
tamanho = len(palavras)
inverso = ''
for c in range(tamanho-1, -1, -1):
    inverso += palavras[c]
if inverso != palavras:
    print('não é um palindromo')
else:
    print('é um palindromo')
print('O inverso de {} é {}' .format(palavras, inverso))