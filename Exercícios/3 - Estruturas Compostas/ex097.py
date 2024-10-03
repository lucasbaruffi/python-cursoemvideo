# Faça um programa que tenha uma função chamada escreva(), que receberá
# um texto qualquer como parâmetro e moestre uma mensagem ocm tamanho 
# adaptável.
# ex:
# escreva('Olá, Mundo!)
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~

def escreva(palavra):
    tamanho = len(palavra) + 4
    print('~'*tamanho)
    print(f'  {palavra}')
    print('~'*tamanho)


# Programa principal
escreva('Gustavo Guanabara')