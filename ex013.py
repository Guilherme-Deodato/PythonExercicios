""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento"""

salario = float(input('Digite o seu salário: '))
aumento = salario + (salario / 100 * 15)

print(f'Parabéns, seu novo salário é {aumento :.2f}!')
