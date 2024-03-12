""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). """


# Meu Jeito
""" n1 = 0
cond = 999
cont = 0
soma = 0

while n1 != cond:
    n1 = int(input("Digite um número: "))
    

    if n1 != 999:
        soma += n1
        cont += 1
    else:
        print("")

    

print("Soma: {} \nNúmeros Digitados: {}".format(soma, cont)) """



# Jeito do Guanabara
n1 = cont = soma = 0
n1 = int(input("Digite um número: "))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input("Digite um número: "))

    

print("Soma: {} \nNúmeros Digitados: {}".format(soma, cont))