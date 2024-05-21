"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = somaterceira = somapares = cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor na posição {l} {c}: "))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]

print('='*30)
print("Matriz".center(30))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]'.center(10), end='')
    print()

for l in range(0, 3):
    somaterceira += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print(f"Soma de todos os valores pares: {somapares}")
print(f"Soma da terceira coluna: {somaterceira}")
print(f"Maior valor da 2 linha: {maior}")