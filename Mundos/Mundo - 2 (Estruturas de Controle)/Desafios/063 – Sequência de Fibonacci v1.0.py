""" Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8 """


n = int(input("Digite um número: "))



cont = 1



while cont != 7:
    a = n + 1
    b = a + a
    
    print("Resultado: {}".format(b))

    

    cont += 1