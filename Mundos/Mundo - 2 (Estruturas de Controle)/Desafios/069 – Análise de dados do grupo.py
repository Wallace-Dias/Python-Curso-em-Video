""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. """


# Ler Idade e Sexo de várias pessoas. [Ok]
# perguntar se o user quer sair ou não[Ok]

# A) quantas pessoas tem mais de 18 anos. [Ok]
# B) quantos homens foram cadastrados. [Ok]
# C) quantas mulheres tem menos de 20 anos. [Ok]

sair = ''

pessoas_maior = 0
homens_cadastrados = 0
mulher_menor = 0
print("="*30)
print("Cadastro".center(30))
print("")
while True:
    print("="*30)
    idade = int(input("Idade: "))
    sexo = ' ' # Obs: se eu não der espaço dentro dessa string ela pula o while seguinte e vai para a verificaço para sair do looping

    while sexo not in 'MF':
        sexo = str(input(("Sexo [M/F]: "))).strip().upper()[0]
    print("="*30)

    # Verifica quantas pessoas tem mais de 18
    if idade >= 18 :
        pessoas_maior += 1

    # Verifica quantos homens foram cadastrados
    if sexo in 'Mm':
        homens_cadastrados +=1
    
    # Verifica quantas Mulheres tem menos de 20
    if idade <20 and sexo in "Ff":
        mulher_menor +=1

    print("\n")
    sair = str(input("Press [S] for Exit and [N/A] to Continue: ")).strip().upper()[0]
    if sair == 'S':
        print("Saindo . . .")
        break

print("\n")
print("Resultados".center(30))
print("="*30)
print(f"Pessoas Maiores de 18: [{pessoas_maior}]")
print(f"\nHomens Cadastrados: [{homens_cadastrados}]")
print(f"\nMulheres com menos de 20: [{mulher_menor}]")
print("="*30)