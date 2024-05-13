""" Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular. """


produtos = ("sabão", 5.00, "veja", 3.40, "escova", 7.90)

print("="*30)
print(f"{'Listagem':^30}")
print("="*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<19}", end='')
    else:
        print(f" R${produtos[pos]:>7.2f}")
    
