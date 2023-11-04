# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
cont = 0
total = 0

for c in range(0, num + 1):
    cont += 1
    print(c)
    if num % cont == 0:
        total += 1
print(f'número {num} foi divisível {total} vezes')
if total ==2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
