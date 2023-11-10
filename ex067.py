# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

cont = 0

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print(37 * '~')
    if num < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    while cont < 10:
        cont +=1
        print(f'{num} x {cont} = {num * cont}')
    cont = 0
