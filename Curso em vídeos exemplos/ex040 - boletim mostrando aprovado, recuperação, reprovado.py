n1 = float(input('Digite qual foi a sua primeira nota'))
n2 = float(input('Digite qual foi a sua segunda nota'))
media = (n1+n2)/2
print('Sua média foi {:.2f}'.format(media))
if media < 5:
    print('Infelizmente, você foi reprovado!')
elif (media >= 5) and (media <= 6.9):
    print('Você está em recuperação!')
else:
    print('Você está aprovado! Parabéns :)')
