n = int(input('digite um número inteiro:'))
primo = 0
for c in range(1,n+1):
    if n%c == 0:
        primo +=1
if primo == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não  é primo.'.format(n))
