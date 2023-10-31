# Cre um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere U$1,00 = 3,27

carteira = float(input('Insira quanto você tem: '))
conversor = carteira * 3.27

print(f'Você tem R${carteira} que equivale a U${conversor:.2f}')
