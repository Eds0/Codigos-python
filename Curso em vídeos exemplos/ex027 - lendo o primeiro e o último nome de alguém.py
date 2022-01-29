nome = str(input('Digite seu nome completo')).strip()
print('Seu nome completo é {}'.format(nome))
nome1= nome.split()
print('Seu primeiro nome é {}'.format(nome1[0]))
nome2 = nome.rfind(' ')
nome3 = nome[nome2+1:]
print('Seu último nome é {}'.format(nome3))
