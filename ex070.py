# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('LOJA SUPER BARATÃO')

total = cont = cont_menor = menor_vlr = 0
menor = ''

while True:
    produto = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$ '))
    cont_menor += 1
    total += valor
    if valor > 1000:
        cont += 1
    if cont_menor == 1 or valor < menor_vlr:
        menor_vlr = valor
        menor = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total em compras foi {total :.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} que custa R${menor_vlr}')
