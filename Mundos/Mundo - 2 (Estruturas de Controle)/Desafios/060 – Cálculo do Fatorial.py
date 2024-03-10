""" Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120 """



n1 = int(input("Digite um número: "))

c = n1
f = 1

while c > 0:
    print("{} ".format(c), end='')
    print("x " if c > 1 else "=", end= '')
    f *= c
    c -= 1

print(" {}".format(f))
print("\nO factorial de {} é = {}".format(n1, f))






# Forma fácil e rápida
""" from math import factorial


n1 = int(input("Digite um número: "))


s = factorial(n1)

print("O factorial de {} é = {}".format(n1, s)) """