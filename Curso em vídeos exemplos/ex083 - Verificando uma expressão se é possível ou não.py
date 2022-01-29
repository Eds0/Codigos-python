expre = str(input('Digite a sua expressão:'))
abre = []
fecha = []
for simb in expre:
    if simb =='(':
        abre.append('(')
    elif simb == ')':
        fecha.append('(')
print(f'Abre: {abre}')
print(f'fecha {fecha}')
if len(abre) == len(fecha):
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')