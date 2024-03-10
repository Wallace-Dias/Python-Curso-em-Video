""" Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer. """



import random

#Desafio 028:
""" Escreva um programa que faça o computador “Pensar” em um número inteiro entre 0 e 5 e peça para o 
usuário tentardescobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se 
o usuário venceu ou perdeu. """


r = random.randint(1, 10)
print("\nNúmero gerado: {}".format(r)) # só para facilitar o teste

ruser = 9 # só para não fazer o input fora do Laço

cont = 0


while r != ruser:
    ruser = int(input("\nAdivinhe o número: "))


    if ruser == r:
        print("Você Acertou!")
    else:
        cont += 1
        if ruser < r:
            print("Mais... Você errou\n")
        if ruser > r:
            print("Menos... Você errou!\n")

print("Você tentou {} vezes".format(cont))