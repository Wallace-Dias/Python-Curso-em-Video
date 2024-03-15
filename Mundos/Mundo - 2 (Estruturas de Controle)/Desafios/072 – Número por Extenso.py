""" Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. """

contagem = ('Zero', 'Um', 'Dois', "Três", "Quatro")
n = int(input("De 0 a 20, Digite um número: "))

print(contagem[n])
