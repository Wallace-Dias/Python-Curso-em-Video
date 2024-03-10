import math
import random
import pygame


#------------------------------------------------------------------------------------------- 
#Desafio 017: Concluído
""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, 
calcule e mostre o comprimento da hipotenusa """

co = float(input("Cateto Oposto: "))
ca =  floatinput(("Cateto Adjacente: "))    
h = (co ** 2 + ca ** 2) ** (1/2)

print("Cateto Oposto: {:.2f} \nCateto Adjacente: {:.2f} \nHipotenusa: {:.2f}".format(co, ca, h))
#-------------------------------------------------------------------------------------------