""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """


lista = [int(input("1° Valor: ")), int(input("2° Valor: ")), int(input("3° Valor: ")), int(input("4° Valor: "))]

maior = menor = posmenor = posmaior = 0
cont = 1

for pos, v in enumerate(lista, start= 1):
    if cont == 1:
        maior = menor = v
        cont += 1
        posmenor = posmaior = pos

    else:

        if v > maior:
            maior = v
            posmaior = pos
        if v < menor:
            menor = v
            posmenor = pos

print(f'\nMaior Valor é = {maior} e está na {posmaior} posição\nMenor Valor = {menor} e está na {posmenor} posição')


        
