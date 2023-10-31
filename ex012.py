# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Insira o valor do produto: '))
desconto = valor - (valor * 0.05)

print(f'Você ganhou desconto na compra e o produto sairá por R${desconto}')
