""" Crie um programa que vai ler vários números e colocar em uma lista.           Depois disso, mostre:
A)Quantos números foram digitados.
B)lista de valores, ordenada de forma decrescente. 
C)Se o valor 5 foi digitado e está ou não na lista. """
lista = []
cinco = False
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break

    # C)
    if n == 5:
        cinco = True
        esq = input("Quer adicionar o Valor a Lista S/N: ")
        if esq in 'Ss':
            lista.append(n)
            
        else:
            n = int(input("Digite um valor: "))
    else:  
        lista.append(n)
    
    

    

    
    
# A)
print('A) - Números Digitados: ',len(lista))

# B)
lista.sort(reverse= True)
print(f'B) - Números Invertidos: {lista}')

# C)
if cinco == True and 5 in lista:
    print("C) - Cinco foi digitado e está na lista")

elif cinco == True and 5 not in lista:
    print("C) - Cinco foi digitado mas não está na lista")

elif cinco == False:
    print("C) - Cinco não foi digitado")