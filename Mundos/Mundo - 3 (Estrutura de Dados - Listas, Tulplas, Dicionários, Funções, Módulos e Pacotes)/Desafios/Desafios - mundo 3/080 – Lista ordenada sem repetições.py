""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. """

lista = []

for i in range(1, 6):

    n = int(input(f"{i}° Valor: "))

    if i == 1 or n > lista[-1]:
        lista.append(n)
            
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos +=1

print("")
for i in lista:
    print(f'{i}...', end='')
