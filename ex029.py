# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual é a velocidade atual do veículo? '))

if velocidade > 80:
    vlr_multa = (velocidade - 80) * 7
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${float(vlr_multa) :.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')
print('Tenha um bom dia! Dirija com segurança!')
