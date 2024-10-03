# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# conceito: "a soma de dois lados é sempre menor que o terceiro lado."

l1 = float(input('Uma reta: '))
l2 = float(input('Outra reta: '))
l3 = float(input('Outra reta: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Sim, é possível montar um triângulo')
else:
    print('Não é possível')

# pegar certificado https://www.cursoemvideo.com/cursos/