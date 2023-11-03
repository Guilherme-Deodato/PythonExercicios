# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (anos * 12)

if parcela > salario * 30 / 100:
    print(f'Para pagar uma casa de R${casa :.2f} em {anos} a prestação será de R${parcela :.2f}')
    print('Empréstimo NEGADO!')
else:
    print(f'Para pagar uma casa de R${casa :.2f} em {anos} a prestação será de R${parcela :.2f}')
    print('Empréstimo pode ser CONCEDIDO!')
