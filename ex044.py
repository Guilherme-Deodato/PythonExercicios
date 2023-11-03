# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Preço das compras: R$'))
pagamento = int(input('''
Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
QUal é a opção? 
'''))

if pagamento == 1:
    desconto = valor - (valor * 0.1)
    print(f'Sua compra de R${valor :.2f} vai custar R${desconto :.2f} no final.')
elif pagamento == 2:
    desconto = valor - (valor * 0.05)
    print(f'Sua compra de R${valor :.2f} vai custar R${desconto :.2f} no final.')
elif pagamento == 3:
    parcelas = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas :.2f} sem juros.')
    print(f'Sua compra custará R${valor :.2f} e não tem desconto.')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    vlr_parcelas = (valor + (valor * 0.2)) / parcelas
    vlr_final = valor + (valor * 0.2)
    print(f'Sua compra será parcelada em {parcelas}x de {vlr_parcelas :.2f} com juros')
    print(f'Sua compra de {valor :.2f} vai custar {vlr_final :.2f} no final.')
else:
    print('Opção invalida, digite uma opção válida.')
