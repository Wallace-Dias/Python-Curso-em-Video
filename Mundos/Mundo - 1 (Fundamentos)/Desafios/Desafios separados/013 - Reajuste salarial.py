#Desafio 013:
#Faça um algoritmo que leia o salário de um funcionário e mostre  seu novo salário, com 15% de aumento.

salario = float(input("Salário do funcionário: R$ "))
novosal = salario + (salario * 15 / 100)

print("Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a ganhar {:.2f} ".format(salario, novosal))

print("-------------------------------------------------------------------------------------")
print("")