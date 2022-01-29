import math
num = float(input('Digite um ângulo:'))
sen = math.sin(math.radians(num))
cose = math.cos(math.radians(num))
ta = math.tan(math.radians(num))
print('O ângulo {}° tem seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}' .format(num,sen,cose,ta))
