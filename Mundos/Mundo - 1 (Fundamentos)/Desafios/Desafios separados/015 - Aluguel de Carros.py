""" Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. """

dias = int(input('Quantos dias Alugado? '))
km = float(input('Quantos Km Rodados? '))
pago = (dias * 60) + (mk * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))
