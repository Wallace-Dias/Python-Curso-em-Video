""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

dic = {'nome': str(input('Nome: '))}
tot = int(input("Quantas partidas: "))
partidas = []

for n in range(1, tot+1):
    partidas.append(int(input(f"Quantos Gols na partida {n}: ")))
dic['gols'] = partidas[:]
dic['total'] = sum(partidas)

print('='*50)
print(dic)
print('='*50)
for k, v in dic.items():
    print(f"{k}: {v}")
print('='*50)
print(f"O jogador {dic['nome']} jogou {len(dic['gols'])} partidas")
for i, v in enumerate(dic['gols']):
    print(f'=> Na partida {i+1} {dic["nome"]} fez {v} Gols')
print(f'Total de Gols: {dic["total"]}')
print('='*50)