""" Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos. """
from time import sleep

n1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
qtd = int(input("Quantos termos: "))
print("")
termo = n1
cont = 1
cont2 = 0


while cont <= qtd:
    print("{}".format(termo), end="")
    print(" -> ", end='')
    termo = termo + r
    cont += 1
    cont2 += 1
    


    if cont > qtd:
        print("\n")
        print("\n[1] - Gerar mais termos \n[2] - Novos termos \n[3] - Sair")
        opc = int(input("\nOpção: "))
        print("\n")

        if opc == 1:
            print("\nMais termos ->")
            qtd = int(input("Quantos termos: "))
            cont = 1
            

        elif opc == 2:
            print("\nNovos termos -> \n")
            print("\n")
            
            n1 = int(input("Primeiro termo: "))
            r = int(input("Razão: "))
            qtd = int(input("Quantos termos: "))
            termo = n1
            cont = 1
            


        elif opc == 3:
            print("Saindo . . .")
            sleep(2)

            


print("Cont {} \nCont2 {}".format(cont, cont2))
print("Progressão finalizada com {} Termos mostrados".format(cont2))
print("\nFim!")

# dif = 1