""" Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares. """

n = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))


print(f"{n}")


# A
a = 0
for c in n:
    if c ==  9:
        a += 1
print(f"O número 9 apareceu {a} vezes")

# B
if 3 in n:
    print(f"O valor 3 está na {n.index(3)+1}° Posição")
else:
    print("O valor 3 não foi digitado")


# C
print("Os valores pares digitados foram: ", end="")
for c in n:
    if c % 2 == 0:
        print(f"{c}, ", end='')


