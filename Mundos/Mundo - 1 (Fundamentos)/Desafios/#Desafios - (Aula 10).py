import random

#Concluído
""" -------------------------------------------------------------------------------------------
Desafio 028:
Escreva um programa que faça o computador “Pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.


r = random.randint(0, 5)
ruser = int(input("Adivinhe o número: "))

if ruser == r:
    print("Você Acertou!")
else:
    print("Você errou")

------------------------------------------------------------------------------------------- """

#Concluído
""" -------------------------------------------------------------------------------------------
Desafio 029:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.


vel = float(input("Velocidade do carro: "))
km = 80
ult = vel - 80
multa = 7*ult

if vel > km:
    print("-----------------------------------------")
    print("Você ultrapassou o limite de velocidadde! \nMulta: R$ {:.2f}".format(multa))
else:
    print("-----------------------------------------")
    print("Você está dentro do limite de Velocidade")
------------------------------------------------------------------------------------------- """    

#Concluído
""" -------------------------------------------------------------------------------------------
Desafio 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.


n1 = int(input("Digite um número: "))

par = n1 % 2

if par == 0:
    print("{} é Par!".format(n1))
else:
    print("{} é Impar!".format(n1))
------------------------------------------------------------------------------------------- """


#Concluído
""" -------------------------------------------------------------------------------------------
Desafio 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas



dist = float(input("Distancia da viagem: "))

pc = 0.50
pl = 0.45

if dist <= 200:
    v1 = pc*dist
    print('---------------------------')
    print("Valor da passagem: R$ {:.2f}".format(v1))
else:
    v2 = pl*dist
    print('---------------------------')
    print("Valor da passagem: R$ {:.2f}".format(v2))

------------------------------------------------------------------------------------------- """



# Concluído
""" -------------------------------------------------------------------------------------------
Desafio 032:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto



# Versão pensada por mim
ano = input("Ano: ")
n1 = input("Quantos dias tem o ano: ")
print("")
if n1 == 366:
    print("-------------------------")
    print("O Ano de {} é um ano bissexto".format(ano))
else:
    print("O Ano de {} não é um ano bissexto".format(ano))


# Versão 2 resolvido pelo guanabara

from datetime import date

ano = int(input("Que ano quer analisar? Coloque 0 para Analisar o ano atual: "))

if ano == 0:
    ano = date.today().year # usado para pegar o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
        #Se o ano for divisivel por 4 e o resto for zero e também não pode ser divisível
        #por 100 ou seja diferente de zero ou então o ano ser divisivel por 400

    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

------------------------------------------------------------------------------------------ """



# Concluído
""" -------------------------------------------------------------------------------------------
Desafio 033:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.



a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
print("")

# Verificando o menor
menor = a
maior = b
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#Verificando o Maior

if a>b and a>c:
    maior = a

if c>a and c>b:
    maior = c

print("-----------------------------")
print("O Menor Valor é {} \nO Maior Valor é {}".format(menor, maior))


------------------------------------------------------------------------------------------- """




# Concluído
""" -------------------------------------------------------------------------------------------
Desafio 034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para Salários superiores a R$ 1.250,00 Calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%


salario = float(input("Salário: "))
print("")

if salario > 1250:
    salario = salario + (salario*0.10)
    print("Você recebeu um aumento de 10% \nSalário Novo: R$ {:.2f}".format(salario))

if salario <= 1250:
    salario = salario + (salario*0.15)
    print("Você recebeu um aumento de 15% \nSalário Novo: R$ {:.2f}".format(salario))


------------------------------------------------------------------------------------------- """



# Concluído
""" -------------------------------------------------------------------------------------------
Desafio 035:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário de elas podem ou não formar um triângulo.


print('-='*20)
print('Analisador de Triângulos')
print('='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo')

------------------------------------------------------------------------------------------- """