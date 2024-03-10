import math
import random
import pygame

#-------------------------------------------------------------------------------------------
#Desafio 019:
""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome deles e escrevendo o nome do escolhido. """

a1 = str(input("Aluno um: "))
a2 = str(input("Aluno dois: "))
a3 = str(input("Aluno três: "))
a4 = str(input("Aluno quatro: "))

lista = [a1, a2, a3, a4]
sort = random.choice(lista)
print("O Aluno Sorteado foi: {}".format(sort))

#-------------------------------------------------------------------------------------------