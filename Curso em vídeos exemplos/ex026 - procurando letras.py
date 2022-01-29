nome = str(input('Digite seu nome completo')).strip().upper()
print('Seu nome possui {} letras A'.format(nome.count('A')))
print('A posição da primeira letra A está {}'.format(nome.find('A')+1))
print('A posição da última letra A está {}'.format(nome.rfind('A')+1))
