# A soma de dois números
n1 = (int(input('Digite um valor: ')))
n2 = (int(input('Digite outro valor: ')))

s = n1 + n2

print('A soma de {} e {} é \033[1;30;107m{}\033[m'.format(n1, n2, s))