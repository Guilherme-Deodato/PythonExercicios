# Um professor quer sortear um dos alunos para apagar o quadro. Faça um programa uqe ajude ele, lendo o nome deles e
# escrevendo o nome escolhido.

from random import choice

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
nomes = [n1, n2, n3, n4]

print(f'O aluno sorteado para limpar o quadro foi {choice(nomes)}!')
