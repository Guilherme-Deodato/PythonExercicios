# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

vlr_entrada = int(input('Insira um valor: '))
dobro = vlr_entrada * 2
triplo = vlr_entrada * 3
raiz = vlr_entrada ** (1/2)

print(
    f'O valor digitado foi {vlr_entrada} \nSeu dobro é igual a {dobro} \nO triplo é igual a {triplo} \nSua raiz {raiz :.2f}'
)
