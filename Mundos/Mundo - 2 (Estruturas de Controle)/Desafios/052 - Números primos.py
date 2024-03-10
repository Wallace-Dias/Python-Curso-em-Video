""" Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

# Número primo tem que ser divisivel por 1 ou ele mesmo
# Tem que continuar sendo inteiro
# Ex: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89 e 97

n1 = int(input("Digite um número: "))
tot = 0

for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        tot += 1
        

    else:
        print('\033[31m', end='')
    
    print("{}".format(c), end= '')

print("\n \033[mO número {} foi divisível {} vezes ".format(n1, tot))

if tot == 2:
    print("{} é um número primo!".format(n1))
else:
    print("{} não é um número primo!".format(n1))



""" if n1 % n1  == 0 or n1:
    print("é um número primo")
    
else: 
    print("não é um número primo") """