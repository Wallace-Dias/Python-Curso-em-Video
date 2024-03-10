#Desafio 010:
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere
#US$ 1,00 = 3.27

real = int(input("Dinheiro: "))
dollar = 3.27

conver1 = real / dollar
conver2 = dollar * real
print("")
print("Compra do dolar")
print("Real: {} --> Dollar {} ".format(real, conver1))

print("")
print("Dollar: {} --> Real {} ".format(real, conver2))

print("-------------------------------------------------------------------------------------")
print("")
