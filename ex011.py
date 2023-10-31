""" Faça um programa que leia a largura e a altura de uma parde em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = altura * largura
tinta = area / 2

print(f'A sua parede te uma área de {area}m² e será necessário {tinta}l de tinta para pinta-lá.')
