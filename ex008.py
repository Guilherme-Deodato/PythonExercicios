# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Insira um valor: '))
centimetros = metros * 100
milimetros = metros * 1000

print('O valor digitado foi {}, é igual a {:.2f} centímetros e {:.2f} milímetros.' .format(metros, centimetros, milimetros))
