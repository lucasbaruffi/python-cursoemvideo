# Crie um módulo chamado moeda.o=py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas func

def metade(v = 0):
    return v / 2

def dobro(v = 0):
    return v * 2

def aumentar(v = 0, p = 0):
    return v + (v/100*p)

def diminuir(v = 0, p = 0):
    return v - (v/100*p)

def moeda(preço = 0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')