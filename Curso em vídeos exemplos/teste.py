
num = list()
positivos = list()
negativos = list()
zeros = list()
for c in range(0,10):
    n = int(input('Digite um número inteiro:'))
for j in range(0,10):
    if num[j] > 0:
        positivos.append(num[j])
    elif num[j] == 0:
        zeros.append(num[j])
    else:
        negativos.append(num[j])

print(positivos)
print(negativos)
print(zeros)
print(len(positivos))
print(len(negativos))
print(len(zeros))
