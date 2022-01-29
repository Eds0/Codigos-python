nome = str(input('Digite o seu nome')).title().strip()
if nome == 'Edson':
    print('Que nome lindo você tem.')
else:
    print('Seu nome é muito comum')
print('Boa tarde, {}'.format(nome))
