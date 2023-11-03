# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

# Função que usa o ano atual da máquina do usuário.
ano = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
ano_alistamento = ano + (18 - idade)
falta_alistar = ano_alistamento - ano
atrasou_alistamento = ano - ano_alistamento

if idade < 18:
    print(f'Quem nasceu em {nasc} tem {idade} em {ano}.')
    print(f'Ainda faltam {falta_alistar} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_alistamento}.')
elif idade > 18:
    print(f'Quem nasceu em {nasc} tem {idade} em {ano}.')
    print(f'Você já deveria ter se alistado há {atrasou_alistamento}.')
    print(f'Seu alistamento foi em {ano_alistamento}.')
elif idade == 18:
    print(f'Quem nasceu em {nasc} tem {idade} em {ano}.')
    print('Você tem que se alistar IMEDIATAMENTE!')
