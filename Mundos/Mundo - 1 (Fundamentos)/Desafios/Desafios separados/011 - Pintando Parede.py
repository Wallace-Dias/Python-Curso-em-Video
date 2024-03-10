#Desafio 011:
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área-
#-e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input("Largura: ")) 
alt = float(input("Altura: "))

area = larg * alt

print("A sua parede tem a dimensão de {}x{} e sua área é de {}m² ".format(larg, alt, area))
print("")

tinta = area / 2
print("Para pintar essa parede você precisará de {}l de tinta".format(tinta))

print("-------------------------------------------------------------------------------------")
print("")