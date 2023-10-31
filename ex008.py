# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Insira uma medida em metros: '))
centimetros = medida * 100
milimetros = medida * 1000

print('O valor digitado foi {}, é igual a {:.2f} centímetros e {:.2f} milímetros.' .format(metros, centimetros, milimetros))
