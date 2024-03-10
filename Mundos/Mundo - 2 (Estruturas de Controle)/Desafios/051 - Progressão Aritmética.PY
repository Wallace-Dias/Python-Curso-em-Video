""" Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão. """


# O que é Progressão Aritmética?
""" Uma progressão aritmética é uma sequência numérica ordenada por uma razão, 
proveniente da subtração de um termo por seu antecessor. """


# Exemplo.: 
""" Progressão arimética é uma sequência numérica em que a diferença entre um termo e seu
antecessor resulta sempre em um mesmo valor, chamado de razão. Por exemplo, considere a sequência a seguir:

(2, 4, 6, 8, 10, 12, 14, 16, 18, 20...)

Vamos observar o que acontece com a subtração de qualquer termo pelos seus antecessores:

20 – 18 = 2

18 – 16 = 2

16 – 14 = 2

14 – 12 = 2 """



n1 = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
décimo = n1 + (10 - 1) * r

for c in range(n1, décimo + r, r):
    print ("{} ".format(c), end='-> ')
print("Acabou")
