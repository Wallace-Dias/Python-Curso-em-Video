from time import sleep
""" Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. """
sair = 0
opc = 0
ini = 0


while sair != 5 and ini != 2:
    if opc != 4:
        ini = int(input("\n[1] - Iniciar Programa\n[2] - Sair do programa\n\nOpção: "))
    

    if ini == 1:
        print("\n")
        n1 = int(input("Valor 1: "))
        n2 = int(input("Valor 2: "))
        print("\n")

        print("\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior/Menor\n[4] - Novos Números\n[5] - Sair do Programa")

        opc = int(input("\nOpção: "))
        print("\n")

        if opc == 1:
            print("Soma dos Valores!\n")

            print("A soma de:\n{} e {} = {}\n".format(n1, n2, n1+n2))



        elif opc == 2:
            print("Multiplicação dos Valores!\n")
            print("A multiplicaçã entre:\n{} x {} = {}".format(n1, n2, n1*n2))
        
        elif opc == 3:
            print("Maior e Menor dos valores!\n")
            if n1 > n2:
                print("{} é Maior que {}".format(n1, n2))
            if n1 < n2:
                print("{} é Menor que {}".format(n1, n2))
            if n1 == n2:
                print("{} e {} são iguais".format(n1, n2))
        
        elif opc == 4:
            print("Novos Números!\n")
            ini = 1

        elif opc == 5:
            print("Saindo do Programa . . .")
            sleep(2)
            ini = 2
        
        elif opc not in (1, 2, 3, 4):
            print("Valor Inválido!")

    elif ini == 2:
        print("Saindo do Programa . . .")
        sleep(2)
        ini = 2

    else:
        print("Valor Inválido!")
