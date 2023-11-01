# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras tem no total (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
junta = nome.replace(' ', '')
dividir = (nome.split())

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(junta)} letras')
print(f'Seu primeiro tem {len(dividir[0])} letras')