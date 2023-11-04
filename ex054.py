# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date

contador = 0
jovem = 0
adulto = 0

for c in range(0, 7):
    contador += 1
    nascimento = int(input(f'Em que ano a {contador}ª pessoa nasceu? '))
    idade = date.today().year - nascimento
    if idade < 18:
        jovem += 1
    else:
        adulto += 1
print(f'Ao todo tivemos {adulto} pessoas maiores de idade')
print(f'E também tivemos {jovem} pessoa menores de idade')

