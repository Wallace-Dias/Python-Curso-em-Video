""" Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. """

#contagem = ('Zero', 'Um', 'Dois', "Três", "Quatro")
contagem = ('Zero', 'Um', 'Dois', "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")



# Jeito do Prof° Guanabara
""" while True:
    núm = int(input("Digite um número entre 0 e 20: "))
    if 0 <= núm <= 20:
        break
    print("tente novamente!")
print(f"Você digitou o número: {cont[núm]}") """












# Meu Jeito
while True:
    entrada = input("Digite um úmero de 0 a 20)")
    if entrada.isdigit():
        n = int(entrada)
        
        #if n >= 0 and n < len(contagem): Outra forma de executar essse if

        #if n >= 0 and n <= len(contagem): este é igual porém tem um <= len(contagem), esse = vai permitir a verificação pois se o user colocar 5 vai funcionar e vai dar erro logo em seguida pois a tupla tem 5 itens mas só vai até o valor 4 por ter 5 o valor 5 vai permitir dando erro na linha seguinte já que contagem[5] não é válido.
    
        if 0 <= n < len(contagem):
            print(contagem[n])
            break
        else:
            print("O número fornecido está fora do intervalo")
else:
    print("Por favor digite apenas números")
    