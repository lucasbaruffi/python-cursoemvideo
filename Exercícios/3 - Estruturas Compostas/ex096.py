# Faça um programa que tenha uma função chamada área(), que receba 
# as dimensões de um terreno retangular (largura e comprimento ) e 
# mostre a área do terreno

def área(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {área:.2f}m²')


# Programa principal
print(' CONTROLE DE TERRENOS ')
print('----------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento(m): '))
área(l, c)