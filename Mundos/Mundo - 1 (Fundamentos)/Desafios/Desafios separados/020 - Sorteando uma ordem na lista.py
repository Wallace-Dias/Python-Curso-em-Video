import math
import random
import pygame

#-------------------------------------------------------------------------------------------
#Desafio 020:
""" O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. """

a1 = str(input("Aluno um: "))
a2 = str(input("Aluno dois: "))
a3 = str(input("Aluno três: "))
a4 = str(input("Aluno quatro: "))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem de sorteio é: ")
print(lista)

#-------------------------------------------------------------------------------------------