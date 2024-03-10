import math
import random
import pygame

#-------------------------------------------------------------------------------------------
# Desafio 016: Concluído
""" Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6. """

n1 = float(input("Digite um número: "))
n1a = math.floor(n1)

print("O número {} tém a parte inteira {} ".format(n1, n1a))
#-------------------------------------------------------------------------------------------