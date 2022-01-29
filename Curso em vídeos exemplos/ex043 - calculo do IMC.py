altura = float(input('Digite a sua altura em metros:'))
peso = float(input('Digite o seu peso em kg:'))
imc = peso/altura**2
print('Seu IMC é {:.2f}'.format(imc))
if imc <18.5:
    print('Você está abaixo do peso')
elif imc>=18.5 and imc<=25:
    print('Você está com o peso ideal')
elif imc>25 and imc<=30:
    print('Você está com sobrepeso')
elif imc>30 and imc<=40:
    print('Você está com obesidade')
elif imc>40:
    print('Você está com obesidade mórbida')
