# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

algo = input('Digite algo:')

print('O tipo primitivo desse valor é', type(algo))
print('É alfanumérico?', algo.isalnum())
print('É alfabético?', algo.isalpha())
print('É um número?', algo.isdigit())
print('Está em minúsculas?', algo.islower())
print('Só tem espaços?', algo.isspace())
print('Está capitalizada?', algo.istitle())
print('Está em maiúsculas?', algo.isupper())
