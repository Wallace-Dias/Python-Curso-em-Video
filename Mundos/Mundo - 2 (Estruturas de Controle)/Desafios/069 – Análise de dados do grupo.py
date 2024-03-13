""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. """


# Ler Idade e Sexo de várias pessoas. [Ok]
# perguntar se o user quer sair ou não[Ok]

# A) quantas pessoas tem mais de 18 anos. [ ]
# B) quantos homens foram cadastrados. [ ]
# C) quantas mulheres tem menos de 20 anos. [ ]

sair = ''

while True:
    idade = int(input("Idade: "))
    sexo = str(input(("Sexo [M/F]: "))).strip().upper()[0]


    sair = str(input("Press [S] for Exit and [N] to Continue")).strip().upper()[0]
    if sair == 'S':
        print("Saindo . . .")
        break
