# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan

angulo = int(input('Digite o valor do angulo: '))

print(f'Para um angulo de {angulo}, seu seno é {sin(angulo)}, o cosseno é {cos(angulo)} e a tangente {tan(angulo)} ')
