"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais
velho e quantas mulheres têm menos de 20 anos. """



# Váriaveis
soma = 0
media = 0
mih = 0
nmv = ('')
totmulher20 = 0

#Mais_novo = 0


# Código Principal
for p in range (1,5):
    print("{}ª Pessoa: ".format(p))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: "))
    print("\n")

    soma += idade # Média da Idade
     
    #mais velho
    if p == 1 and sexo in 'Mm':
        mih = idade
        nmv = nome
        #Mais_novo = idade

    if sexo in 'Mm' and idade > mih:
        mih = idade
        nmv = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        
        #Jeito errado que eu fiz
    """ else:
        if idade > Mais_velho:
            Mais_velho = idade
            nmv = nome

        if idade < Mais_novo:
            Mais_novo = idade
        
        # homem mais velho
        if sexo == "M" and idade == Mais_velho:
            shv = nome
#----------------------------------------------------------
# Geito do Chat GPT
    if a == 1 or idade > Mais_velho:
        Mais_velho = idade
        nmv = nome

    # mais novo
    if idade < Mais_novo:
        Mais_novo = idade

    # homem mais velho
    if sexo == "M" and idade == Mais_velho:
        shv = nome """

        

        

        
    
print("\n")

# Média da Idade
media = soma / a

print("Média das Idades é {}".format(media))
print("{} é o Homem mais velho e tem {} anos".format(nmv, mih))
print("O total de mulheres com menos de 20 anos é {}".format(totmulher20))




#Informaçoes desnecessárias que pedi
""" print("{} é a pessoa mais velha com {} anos".format(nmv, Mais_velho))
print("{} é o Homem mais velho mais velho".format(shv)) """

""" if sex == ('M'):
    print("O mais velho é Homem e é o {}".format(nmv))
    
else:
    print("Sex Failed") """
    



# Nome do Homem mais velho
#print("O mais velho é {}".format(Mais_velho))
#print("O mais novo é {}".format(Mais_novo))












#Rascunho
""" soma = 0 
for n in range (1,4):
    nota = int(input("{}ª Nota: ".format(n)))
    soma = soma + nota


media = soma / n

print("A média é {}".format(media)) """