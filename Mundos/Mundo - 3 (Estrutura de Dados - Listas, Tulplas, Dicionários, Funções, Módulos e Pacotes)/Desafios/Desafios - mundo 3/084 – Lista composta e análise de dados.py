""" Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final,
mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. """

pessoas = []
pesada = leve = tot = 0
for c in range (0, 5):
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    pessoas.append(nome)
    pessoas.append(peso)
    tot += 1

# A) Quantas pessoas foram cadastradas:
print(f"Foram cadastradas {tot} pessoas")

#B) Lista de pessoas mais pessadas: 
for c in pessoas:
    if peso >= 100:
        
        print(f"Pessoas Pesadas:\n{c}")
    else:
        print(f'Pessoas Leves:\n{c}')

    

