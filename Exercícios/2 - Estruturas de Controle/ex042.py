# Refaça o desafio 035 , acrescentando o recurso de mostrar que tipo de
# tinângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes


l1 = float(input('Uma reta: '))
l2 = float(input('Outra reta: '))
l3 = float(input('Outra reta: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Sim, é possível montar um triângulo')
    if l1 == l2 == l3:
        print('Será um triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Será um triângulo Isósceles')
    else:
        print('Será um triângulo Escaleno')
else:
    print('Não é possível')

# pegar certificado https://www.cursoemvideo.com/cursos/