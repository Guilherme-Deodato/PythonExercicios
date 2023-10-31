# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o valor do angulo: '))


print(f'Para um angulo de {angulo}, seu seno é {math.sin(math.radians(angulo)) :.2f}, o cosseno é {math.cos(math.radians(angulo)) :.2f} e a tangente {math.tan(math.radians(angulo)) :.2f} ')
