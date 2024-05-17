""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas. """

lista = []
listb = []
listc = []

while True:
    n = int(input("Digite um valor: "))
    if n == 0:
        break
    lista.append(n)

for i in lista:
    if i % 2 == 0:
        listb.append(i)
    else:
        listc.append(i)

print(f'Primeira Lista: {lista}')

print(f"Lista com Valores Pares: {listb}")

print(f"Lista com Valores Impares: {listc}")