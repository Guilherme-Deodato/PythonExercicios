''' Faça um programa que leia o comprimento do cateto oposto e do cateto ajacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot

cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))

print(f'O valor da hipotenusa é {hypot(cat_oposto, cat_adjacente) :.2f}')
