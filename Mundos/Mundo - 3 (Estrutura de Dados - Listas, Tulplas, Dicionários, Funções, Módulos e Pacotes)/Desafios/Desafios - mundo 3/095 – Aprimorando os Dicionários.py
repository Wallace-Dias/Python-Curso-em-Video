""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""



""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. """

# Resolução do guanabara
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador = {'nome': str(input('Nome: '))}
    tot = int(input("Quantas partidas: "))
    partidas.clear()


    for c in range(0, tot):
        partidas.append(int(input(f"Quantos Gols na partida {c+1}: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in 'SN':
            break
        print("Erro! Responda apenas com S ou N.")
    if resp == 'N':
        break
        
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()

print('-'*40)

for k, v in enumerate(time):

    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('-'*40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! não existe jogador com código {busca}!")
    else:
        print(f" -- Levantamento do jogador {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No jogo  {i+1} fez {g} gols.")
    print("-"*40)
print("<< Volte Sempre >>")










#Minha gambiarra incompleta
""" time = []
# jogador = {'nome': Wallace, 'gols':  [2, 3, 4], 'total': 9}
# partidas = [2, 3, 4]
# time = [{'nome': Wallace, 'gols':  [2, 3, 4], 'total': 9}]

while True:
    opc = int(input("\n[1] - Add jogador \n[2] - Time \n[3] - Pesquisar \n[4] - Sair \nOpc: "))
    # Cadastrar 
    if opc == 1:
        print("")
        jogador = {'nome': str(input('Nome: '))}
        tot = int(input("Quantas partidas: "))
        partidas = []

        for n in range(1, tot+1):
            partidas.append(int(input(f"Quantos Gols na partida {n}: ")))

        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        time.append(jogador.copy())
        jogador.clear()


    # Listar Time
    elif opc == 2:
        print("-"*50)
        
        for i in time:
            print(f"COD", end='')    
            for k in i.keys():
                print(f"{k:>15}", end='')
            print()
            for index, v in enumerate(i.values(), start=1):
                print(f" {index} {str(v):>15}", end=''.center(15))
            print()
        
        print("-"*50)

        for i in time:
            print("="*30)
            for k, v in i.items():
                print(f"{k}: {v}")
            print("="*30)
        
     # Pesquisar
    elif opc == 3:
        pesq = int(input("N° do Jogador: "))
        if pesq == 999:
            break

        elif pesq >= len(time):
            print(f"Erro, não existe jogador com o código {pesq}")

        else:
            print(f"Levantamento do Jogador {time[pesq]['nome']}")
            for i, g in enumerate (time[pesq]['gols']):
                print()

    elif opc == 4:
        break

    else:
        print("Valor Incorreto") """





# -------------








# -------------



""" print('='*50)
print(dic)


print('='*50)


for k, v in dic.items():


    print(f"{k}: {v}")


print('='*50)


print(f"O jogador {dic['nome']} jogou {len(dic['gols'])} partidas")


for i, v in enumerate(dic['gols']):


    print(f'=> Na partida {i+1} {dic["nome"]} fez {v} Gols')


print(f'Total de Gols: {dic["total"]}')


print('='*50) """