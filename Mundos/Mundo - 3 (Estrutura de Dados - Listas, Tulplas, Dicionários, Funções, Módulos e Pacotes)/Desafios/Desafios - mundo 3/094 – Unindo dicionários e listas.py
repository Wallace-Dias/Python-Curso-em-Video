""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média """
# [x] - Ler nome, sexo e idade de várias pessoas guardando um dicionário.
# [x] - Guardar todos os dicionários em uma lista.
# [x] - Mostre quantas pessoas foram cadastradas
# [x] - Mostre a média de idade.
# [x] - Mostre uma lista com as mulheres.
# [x] - Mostre uma lista de pessoas com idade acima da média.

temp = {}
pessoas = []
soma = media = 0
# pessoas = [{Nome: Wallace, Sexo: M, Idade: 23}, {}]

while True:
    temp.clear()
    while True:
        opc = input("Add People? \n[1] - Sim | [2] - Não: ")
        if opc.isdigit():
            opc = int(opc)
            break
        print("Digite apenas números")

    
    if opc == 1:    
        temp['nome'] = str(input('Nome: '))
        while True:
            temp['sexo'] = str(input("Sexo M/F: ")).upper()[0]
            if temp['sexo'] in 'MF':
                break
            print("Insira M ou F")
        while True:
            temp['idade'] = (input("Idade: "))
            if temp['idade'].isdigit():
                temp['idade'] = int(temp['idade'])
                soma += temp['idade']
                break
            print("Digite apenas números!")
        pessoas.append(temp.copy())
    

    elif opc == 2:
        break
    else: 
        print("Valor inválido")
print("")    

# Quantas pessoas foram cadastradas
print(f"Pessoas cadastradas: {len(pessoas)}")

# Média de Idade
media = int(soma / len(pessoas))
print(f'Média de Idade: {media}')

# Lista com mulheres
print("Mulheres Cadastradas: ", end='')
for i in pessoas:
    if i['sexo'] in "F":
        print(f"{i['nome']}", end=', ')
print()

# Pessoas acima da média
print("Pessoas acima da média")
for p in pessoas:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f"{k} = {v}")
"""    
print("Temp")
print(temp)
print("="*30)
print("pessoas")
print(pessoas)
print("="*30)


 """
