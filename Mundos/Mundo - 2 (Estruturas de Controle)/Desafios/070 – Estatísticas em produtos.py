""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. """


# Ler nome e preço de vários produtos - [Ok]
# Perguntar user se quer continuar sim ou não - [Ok]
#A) qual é o total gasto na compra - [Ok]
#B) quantos produtos custam mais de R$1000 - [Ok]
#C) qual é o nome do produto mais barato - [Ok]
print("\n")
sair = ' '
soma = 0
maior = 0
menor = 0
mais_barato = ' '
cont = 0
print("="*30)
print("Compras")

while True:
    # Ler nome e preço de produtos
    print("="*30)
    produto = str(input(('Nome do Produto: '))).strip().capitalize()
    preço = float(input("Preço R$ "))
    print("="*30)
    # Total gasto na compra
    soma += preço
    cont += 1
    sair = " "

    # Quantos produtos custão mais de R$ 1.000
    if preço > 1000:
        maior += 1

    # Nome do produto mais barato
    if cont == 1 or preço < menor:
        menor = preço
        mais_barato = produto




    # Sair do Looping
    while sair not in 'SN':
        sair = str(input(("[S] - Continue / [N] - Exit: "))).strip().upper()[0]
    print("")
    if sair == 'N':
        print("Saindo . . .")
        break

print("\n")
print("Nota Fiscal".center(60)) # só de memes
print("="*60)


print(f"Total gasto na compra: R$ {soma:.2f}")
print(f"Produtos que custão mais de R$ 1.000 [{maior}]")
print(f"Produto mais barato: {mais_barato} no valor de R$ {menor:.2f}")



print("="*60)
print("\n")
print("{:=^60}".format("Fim do programa")) # Teste, acabei de descobrir essa formatação