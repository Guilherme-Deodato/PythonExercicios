# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

cont_1 = 0

num = int(input('Digite um número para ver sua tabuada: '))

for cont in range(0, 10):
    cont_1 += 1
    print(f'{num} x {cont_1} = {num * cont_1}')
