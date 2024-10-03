# Crie um programa que tenha um atupla única com nomes de produtos e seus
# respectivos preços, na sequência.
# No final, mostre uma liustagem de preços, organizando os dados de forma tabular

listagem = ('Lápis', 1.75, 
            'Borracha', 2, 
            'Caderno', 15.9,
            'Estojo', 25, 
            'Transferidor', 4.2, 
            'Compasso', 9.99,
            'Mochila', 120.32, 
            'Canetas', 22.3, 
            'Livro', 34.9)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

itens = listagem[0::2]
preços = listagem[1::2]
preço = 0
for item in itens:
    print(f'{item:.<30}R$', end='')
    print('{: >8.2f}'.format(preços[preço]))
    preço += 1
print('-'*40)
