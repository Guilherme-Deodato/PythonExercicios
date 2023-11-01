# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Você está prestes a começar um viagem de {distancia}Km.')
    print(f'E o preço da sua passagem será de R${valor :.2f}')
else:
    valor = distancia * 0.45
    print(f'Você está prestes a começar um viagem de {distancia}Km.')
    print(f'E o preço da sua passagem será de R${valor :.2f}')
