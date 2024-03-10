""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto. """


#Meu Jeito
""" a = 0
while a != 1:
    n = str(input("Qual o seu sexo: "))

    if n in'MmFf':
        print("Seu Sexo é {}\n".format(n))
        a = 1
    else:
        print("Digite novamente! \n") """


#Jeito do guanabara
print("\n\n")
sexo = str(input("Qual é o seu sexo [M/F] : ")).strip().upper()[0] # esse [0] é um fatiamento onde apenas a primeira letra do que for digitado sera pegada

while sexo not in 'MmFf':
    sexo = str(input("\nValor Inválido, digite novamente! \nQual é o seu sexo?: ")).strip().upper()[0]
    
print("\nSexo {} registrado com susesso!".format(sexo))