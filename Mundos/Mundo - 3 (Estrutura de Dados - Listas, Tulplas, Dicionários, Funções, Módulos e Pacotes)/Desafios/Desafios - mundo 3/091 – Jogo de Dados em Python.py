""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. """

from random import randint
from operator import itemgetter

p1 = randint(1,6)
p2 = randint(1,6)
p3 = randint(1,6)
p4 = randint(1,6)


dic = {'P1': p1, 'P2': p2, 'P3': p3, 'P4': p4}
ranking = {}

for i, v in dic.items():
    print(f'{i} Tirou {v} no dado')

ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
print("")

for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')



