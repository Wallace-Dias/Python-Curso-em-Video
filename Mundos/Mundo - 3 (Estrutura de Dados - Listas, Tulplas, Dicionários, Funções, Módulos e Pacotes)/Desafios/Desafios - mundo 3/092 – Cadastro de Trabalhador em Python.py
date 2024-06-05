""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """
# [x] - Ler Nome [x]/ Ano de Nascimento [x] e CTPS [x]
# [x] - Cadastrar idade atual
# [x] - Se ctps for diferente de 0 mostrar ano de contratação e o salário
# [x] - Com quantos anos a pessoa vai se aposentar

from datetime import datetime
dados = {}

dados['nome'] = str(input("Nome: "))
dados['ano'] = int(input("Que ano nasceu: "))
dados['ctps'] = int(input("CTPS / 0 - não tem: "))

ano_atual = datetime.now().year
dados['idade'] = ano_atual - dados['ano']


if dados['ctps'] != 0:
    dados['contrato'] = int(input("Ano de Contratação: "))
    dados['salário'] = float(input("Salário: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrato'] + 35) - datetime.now().year)
    
    
else:
    print("Não tem CTPS")
print("")

print('='*30)
for k, v in dados.items():
    print(f'{k}: {v}')