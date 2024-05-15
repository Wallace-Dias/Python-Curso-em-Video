""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """

lista = []
pos = 1


while True:

    n = int(input(f"{pos}° Valor: "))
    pos +=1

    if n not in lista:
        lista.append(n)
        print("Valor adicionado!\n")

    else: 
        print("\nValor duplicado")
        r = input("Quer continuar S/N? ")
        if r in 'Nn':
            break

print("\n")
for i in sorted(lista):
    print(f"{i}...", end='')