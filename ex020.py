# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de tabralhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome1 = input('Digite o nome do 1º aluno: ')
nome2 = input('Digite o nome do 2º aluno: ')
nome3 = input('Digite o nome do 3º aluno: ')
nome4 = input('Digite o nome do 4º aluno: ')
nomes = [nome1, nome2, nome3, nome4]

shuffle(nomes)

print(f'A ordem de apresentação será {nomes}')
