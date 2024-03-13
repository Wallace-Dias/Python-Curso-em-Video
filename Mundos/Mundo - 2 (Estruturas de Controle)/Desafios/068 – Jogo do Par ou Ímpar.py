""" Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """
import random

# Quando errar o user errar a letra e colocar errado tem que repetir a pergunta [ ]

# Formatar e dar espaços [ ]


vit = 0
cal = 0
print("="*30)
print("Par ou Impar".center(30))
print("="*30)

while True:
    c = random.randint(1, 10)
    print(f"Dica: {c}")
    p1 = str(input("Par ou Impar: [P/I]:  ".rjust(23))).strip().upper() [0]
    p2 = int(input("Quanto quer jogar? ".rjust(23)))

    cal = (c + p2) % 2

    if p1 == 'P' and cal == 0 or p1 == 'I' and cal == 1:
        print("\n")
        print("="*30)
        print("Vitória!".center(30))
        print(f"Teste de Cal: {cal}")
        print("="*30)
        print("\n")
        print(f"Jogador: {p1}".center(30))
        print(f"Computador: {c}".center(30))
        print("="*30)
        vit += 1
    
    else:
        print("\n")
        print("="*30)
        print("Derrota".center(30))
        print(f"Teste de Cal: {cal}")
        print("="*30)

        print(f"Jogador: {p1}".center(30))
        print(f"Computador: {c}".center(30))
        print("="*30)
        break
print("\n")
print("="*30)
print(f"Vitórias {vit}".center(30))
print("="*30)
