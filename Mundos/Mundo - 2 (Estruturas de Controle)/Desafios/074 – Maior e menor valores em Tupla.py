""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. """

from random import randint


números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))



# Meu jeito

""" menor = números
maior = números
cont = 0
for c in números:
    cont += 1
    if cont == 1:
        maior = c
        menor = c

    elif c > maior:
        maior = c
    elif c < menor:
        menor = c 

    else:
        break
    
print(f"Sorteio {números}")
print(f"Menor n°{menor}")
print(f"Maior n°{maior}")
 """

# Jeito do guanabara
print("Os números sorteados foram:\n")
print("Números: ", end='')
for c in números:
    print(f"{c},", end="")
    
print("")
print(f"Menor n°{min(números)}")
print(f"Maior n°{max(números)}")

    