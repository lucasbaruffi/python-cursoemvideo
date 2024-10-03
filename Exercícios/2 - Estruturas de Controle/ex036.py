# Escreva um programa para aprovar o empréstimo bancário para a 
# compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

v_casa = float(input('Qual valor da casa? '))
sal = float(input('Qual o seu salário? '))
qtd_ano = int(input('Quer pagar em quantos anos? '))

qtd_mes = qtd_ano*12
vlr_mes = v_casa/qtd_mes

print('Você pagaria R${:.2f} por mês'.format(vlr_mes))

porcent = vlr_mes/sal*100

if porcent > 30:
    print('Empréstimo \033[31mNEGADO\033[m, o valor da parcela é {:.0f}% do seu salário'.format(porcent))
else:
    print('Emprésitimo \033[32mAPROVADO\033[m, o valor da parcela é apenas {:.0f}% do seu salário'.format(porcent))    

