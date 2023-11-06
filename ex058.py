#  Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#  Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
''')
acertou = False
sorteio = randint(0,10)
tentativa = 0

while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    if palpite < sorteio:
        print('Mais... Tente mais uma vez.')
        tentativa += 1
    if palpite > sorteio:
        print('Menos... Tente mais uma vez.')
        tentativa += 1
    if palpite == sorteio:
        acertou = True
        tentativa += 1
        print(f'Acertou com {tentativa} tentativas. Parabéns!')
