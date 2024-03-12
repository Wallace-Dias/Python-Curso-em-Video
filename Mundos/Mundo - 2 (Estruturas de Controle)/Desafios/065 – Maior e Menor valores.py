""" Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. """


# Ler Vários n° - [Ok]
# Mostrar Média - [Ok]
# Maior e menor - [Ok]
# Confirm user  - [Ok]

n = cond = cont = maior = menor = soma = 0
n = int(input("\nPara Sair Digite [502] \nDigite um número: "))
while n != 502:
    soma += n
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont+= 1
    n = int(input("\nPara Sair Digite [502] \nDigite um número: "))
media = soma / cont
print("média: {} \nMaior n° {} \nMenor n° {}".format(media, maior, menor))
print("Contador: {}".format(cont))
