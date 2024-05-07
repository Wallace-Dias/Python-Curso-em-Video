""" Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. """

lista = ("Tedio", "Decepçao", "Depressao")

for p in lista:
    print(f"\nNa palavra {p.upper()} Temos: ", end='')
    
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end='')

