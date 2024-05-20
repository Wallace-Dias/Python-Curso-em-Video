""" Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final,
mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. """

temp = [] # Exemplo temp = [nome[0] peso[1]]

principal = [] # Exemplo principal = [[nome, peso] 0, [nome, peso] 1]
maior = menor = tot = 0
for c in range (0, 6):
    temp.append(str(input("Nome: "))) # 0
    temp.append(float(input("Peso: "))) # 1

    if len(principal) == 0:
        maior = menor = temp[1]

    else:
        if temp[1] > maior:
            maior = temp[1]

        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()

    tot += 1

# A) Quantas pessoas foram cadastradas:
print(f"Foram cadastradas {tot} pessoas")

#B) Lista de pessoas mais pessadas:
print(f"O maior peso foi {maior}")
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')

print(f"O menor peso foi {menor}")
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}")


    

    

