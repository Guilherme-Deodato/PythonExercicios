# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

sorteio = randint(0,11)
vitória = 0

while True:
    valor = int(input('Digite um valor de [0 à 10]: '))
    escolha = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    if escolha == 'P':
        resultado = (valor + sorteio) % 2
        if resultado == 0:
            print(f'Você jogou {valor} e o computador jogou {sorteio}. Total de {valor + sorteio} DEU PAR')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitória += 1
        elif resultado != 0:
            print(f'Você jogou {valor} e o computador {sorteio}. Total de {valor + sorteio} DEU ÍMPAR')
            print('Você PERDEU!')
            print(f'GAME OVER! Você venceu {vitória} vezes')
            break
    if escolha == 'I':
        resultado = (valor + sorteio) % 2
        if resultado != 0:
            print(f'Você jogou {valor} e o computador {sorteio}. Total de {valor + sorteio} DEU ÍMPAR')
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            vitória += 1
        elif resultado == 0:
            print(f'Você jogou {valor} e o computador jogou {sorteio}. Total de {valor + sorteio} DEU PAR')
            print('Você PERDEU!')
            print(f'GAME OVER! Você venceu {vitória} vezes')
            break
    elif escolha != 'P' and 'I':
        print('Opção desconhecida, tente novamente...')
