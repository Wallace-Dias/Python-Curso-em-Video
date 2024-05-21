""" Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. """

""" matriz = [[],[], [],
          [], [], [],
          [], [], []] """

# jeito do prof°
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor na posição {l} {c}: "))

print('='*30)
print("Matriz".center(30))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]'.center(10), end='')
    print()
















""" # Minha Versão
matriz = []

# matriz = [[0],[1], [2],
#          [3], [4], [5],
#          [6], [7], [8]]
print(len(matriz))

#for c in len(matriz):
while len(matriz) < 9:
    n = int(input("Valor: "))
    matriz.append(n)

print("="*30)
print("Matriz".center(30))
print("="*30)
print(f"[{matriz[0]}] [{matriz[1]}] [{matriz[2]}]".center(30))
print(f"[{matriz[3]}] [{matriz[4]}] [{matriz[5]}]".center(30))
print(f"[{matriz[6]}] [{matriz[7]}] [{matriz[8]}]".center(30))
print("="*30) """