#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#  No final do programa, mostre:
#  a média de idade do grupo,
#  qual é o nome do homem mais velho
#  quantas mulheres têm menos de 20 anos.

soma = 0
mais_velho = 0
nome_velho = 0
mulher_jovem = 0

for c in range(1, 5):
    print(f'---- {c} Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if sexo == 'Mm':
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_jovem += 1

media = soma / 4
print(f'A média de idade do grupo é de {media :.1f}')
print(f'O homem mais velho tem {mais_velho} e se chama {nome_velho}.')
print(f'Ao todo são {mulher_jovem} mulheres com menos de 20 anos.')
