# Crie um módulo chamado moeda.o=py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas func

def metade(v=0, f=False):
    m = v / 2
    if f:
        return moeda(m)
    else:
        return m

def dobro(v=0, f=False):
    d = v * 2
    if f:
        return(moeda(d))
    else:
        return d

def aumentar(v=0, p=0, f=False):
    a = v + (v/100*p)
    if f:
        return(moeda(a))
    else:
        return a

def diminuir(v=0, p=0, f=False):
    d = v - (v/100*p)
    if f:
        return (moeda(d))
    else:
        return d

def moeda(preço = 0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')