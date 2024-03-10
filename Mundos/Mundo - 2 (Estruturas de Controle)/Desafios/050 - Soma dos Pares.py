""" Exercício Python 050: Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. """
soma = 0
cont = 0

for c in range(1,7):
    n1 = int(input("N° {}: ".format(c)))
    if n1 % 2 == 0: # condição para só somar se o numero for par
        soma = soma + n1 # poderia ser: soma += n1 (daria o mesmo)
        cont = cont +1 # poderia ser: cont += 1 (daria o mesmo)

print("Você informou {} números PARES e a soma é {} ".format(cont, soma))