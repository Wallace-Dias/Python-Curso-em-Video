""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. """
from random import randint
from time import sleep
temp = []
principal = []
cont = 0
esq = int(input("quantos jogos você quer?: "))
while cont != esq:
    tot = 0
    while True:
        n = randint(1,60)
        if n not in temp:
            temp.append(n)
            tot += 1
        if tot >= 6:
            break


    principal.append(temp[:])
    temp.clear()
    cont +=1

v = 40
print('='*v)
print("Mega Sena".center(v))
print('='*v)


for index, c in enumerate(sorted(principal), start=1):
    if index <= 9: # apenas para o print ficar assimétrico caso pase de 9 jogos
        print(f'{index}° Jogo:  ', end='')
        for i in sorted(c):
            print(f'[{i:^2}] ',end='')
        print()
        sleep(1)
    else:
        print(f'{index}° Jogo: ', end='') # a diferença está em um espaço a menos
        for i in sorted(c):
            print(f'[{i:^2}] ',end='')
        print()
        sleep(1)
print('='*v)
    