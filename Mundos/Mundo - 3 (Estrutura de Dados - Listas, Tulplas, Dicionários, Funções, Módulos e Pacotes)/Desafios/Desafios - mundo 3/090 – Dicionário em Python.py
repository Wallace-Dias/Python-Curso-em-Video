""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. """

aluno = {}

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Média: "))

if aluno['media'] <= 4.9:
    aluno['Situação'] = 'Reprovado'
#elif aluno['media'] >= 5 and aluno['media'] <= 5.9:
elif  5 <= aluno['media'] <= 5.9 :
    aluno['Situação'] =  'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'{k} {v}')