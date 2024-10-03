# Crie um programa que tenha uma função fatorial() que receba dois 
# parâmetros: o primeiro que indique o número a calcular e o outro
# chamado show, que será um valor lógico (opcional) indicando se 
# será mostrado ou não na sua tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :paran n: O número a ser calculado.
    :paran show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """


    soma = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        soma *= c
    return(soma)

print(fatorial(5, show=True))