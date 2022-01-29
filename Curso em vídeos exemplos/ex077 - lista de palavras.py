a = (str(input('Digite uma palavra:')).strip(),
     str(input('Digite uma palavra:')).strip(),
     str(input('Digite uma palavra:')).strip(),
     str(input('Digite uma palavra:')).strip(),
     str(input('Digite uma palavra:')).strip())
for palavras in a:
    print(f'\nEm {palavras.upper()} tem as vogais:')
    for letras in palavras:
        if letras in 'aeiou':
            print(letras,end=' ')
