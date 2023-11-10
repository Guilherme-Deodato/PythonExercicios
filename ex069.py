# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print(37 * '~')
print('CADASTRE UMA PESSOA')
cont_idade = 0
cont_m = 0
cont_f = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]').strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade <= 20:
        cont_f += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Ao todo temos {cont_m} homens cadastrados')
print(f'E temos {cont_f} mulheres com menos de 20 anos')
