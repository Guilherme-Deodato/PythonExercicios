# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
finalizar = False

while not finalizar:
    escolha = int(input('''
        [ 1 ] somar
        [ 2 ] multiplicar 
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        >>>>> Qual é a sua opção? 
    '''))
    soma = num1 + num2
    divisor = num1 * num2
    maior = 0
    if escolha == 1:
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif escolha == 2:
        print(f'O resultado de {num1} x {num2} é {divisor}')
    elif escolha == 3:
        if num1 > num2:
            maior = num1
            print(f'Entre {num1} e {num2} o maior é {maior}')
        else:
            maior = num2
            print(f'Entre {num1} e {num2} o maior é {maior}')
    elif escolha == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    if escolha == 5:
        finalizar = True
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre!')
