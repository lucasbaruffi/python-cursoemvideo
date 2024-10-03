# Crie um módulo chamado moeda.o=py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas func

def metade(v):
    return v / 2

def dobro(v):
    return v * 2

def aumentar(v, p):
    return v + (v/100*p)

def diminuir(v, p):
    return v - (v/100*p)
