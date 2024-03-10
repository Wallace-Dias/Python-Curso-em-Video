import math
import random
import pygame

""" Nota: quando quiser fazer um comentário englobando tudo você seleciona o texto e aperta Shift + Alt + a """

#-------------------------------------------------------------------------------------------
#Desafio 021:
""" Faça um programa em python que abra e reproduza o áudio de um arquivo MP3. """




pygame.init()
pygame.mixer.music.load("lonely.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

# Enquanto Xie
#não aceitar o desconforto para manter o conforto de outra pessoa