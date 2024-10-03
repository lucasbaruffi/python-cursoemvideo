# Escrevaum programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

v = float(input('Digite um valor em metros: '))

# Centímetros
c = v*100

# Milímetros
m = v*1000

print('{} metros são iguais à {} centímetros e {} milímetros'.format(v,c,m))