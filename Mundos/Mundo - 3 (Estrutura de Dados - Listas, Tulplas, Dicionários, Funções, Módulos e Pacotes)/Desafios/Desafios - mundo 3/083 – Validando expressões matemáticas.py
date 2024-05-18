""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. """

expressão = str(input("Digite a expressão: "))
a = 0
f = 0

for i in expressão:

    if i == '(':
        a +=1
    elif i == ')':
        f += 1

if a == f:
    print('Expressão válida!')
    print(f'Abertos: {a} Fechados: {f}')
else:
    print('Expressão Inválida! ')
    print(f'Abertos: {a} Fechados: {f}')