# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from random import randint

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
sorteio = randint(0, 5)  # Sorteia um número entre 0 e 5

if jogador == sorteio:
    print('Processando...')
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Processando...')
    print(f'Ganhei! eu pensei no número {sorteio} e não {jogador}')
