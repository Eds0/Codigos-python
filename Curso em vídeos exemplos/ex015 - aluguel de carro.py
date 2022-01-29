d = int(input('Quantos dias você irá alugar o carro?'))
km = int(input('Quantos quilômetros você pretende percorrer?'))
t = 60*d+km*0.15
print('Total a pagar será {:.2f} R$'.format(t))
