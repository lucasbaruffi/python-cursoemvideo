# Crie um módulo chamado moeda.o=py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas func

def título(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

def linha():
    print('-'*30)

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

def resumo(v=0, aum=0, dim=0):
    global dobro
    global metade
    global aumentar
    global diminuir
    dobro = dobro(v, True)
    metade = metade(v, True)
    aument = aumentar(v, aum, True)
    dimin = diminuir(v, dim, True)

    título('RESUMO DO VALOR')

    print(f'''{'Preço analisado:':<20}{moeda(v):<10}
{'Dobro do preço:':<20}{dobro:<10}
{'Metade do preço:':<20}{metade:<10}
{f'{aum}% de aumento:':<20}{aument:<10}
{f'{dim}% de redução:':<20}{dimin:<10}''')
    linha()