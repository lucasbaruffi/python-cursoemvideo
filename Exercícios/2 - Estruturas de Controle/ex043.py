# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status< de acordo com a tebela abaixo:
# abaixo de 18.5: Abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

# IMC = peso / altura^2

peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/altura**2

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc>= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')