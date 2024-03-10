import math
import random
import pygame

#-------------------------------------------------------------------------------------------
#Desafio 018: Concluído
""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. """

ang = float(input("Digite um angulo: "))

sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))

print("Considerando o Ângulo: {:.2f} \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}".format(ang, sen, cos, tang))

#-------------------------------------------------------------------------------------------