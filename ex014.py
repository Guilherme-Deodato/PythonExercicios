''' Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

celsius = float(input('Insira a temperatura ºC:'))
conversor = celsius * 9/5 + 32

print(f'A temperatura de {celsius}ºC corresponde a {conversor}ºF!')
