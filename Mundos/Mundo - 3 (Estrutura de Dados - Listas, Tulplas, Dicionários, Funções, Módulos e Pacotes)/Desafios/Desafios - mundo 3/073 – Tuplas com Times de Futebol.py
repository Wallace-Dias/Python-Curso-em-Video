""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense. """



times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoence", "Vasco", "Atlético", "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritíba", "Avaí", "Ponte Preta", "Atlético-GO")

n = 0
print("Lista de times: ")
for pos, c in enumerate (times, start=1):
    print(f"{pos}, {c}\n")
    n += 1
    if n == len(times):
        break


# A) Os 5 primeiros times.
print(f"Os 5 Primeiros são {times[0:5]}")

# B) Os últimos 4 colocados.
print(f"Os 4 últimos colocados são {times[-4:]}")

# C) Times em ordem alfabética.
print("\n")
print(sorted(times), end=" ") 

# D) Em que posição está o time da Chapecoense.
print("\n")
print(f"O time da Chapecoense está na {times.index('Chapecoence')+ 1}° posição") # Chapecoence está com aspas simples pq estava dando erro com as duplas por ele já estar dentro de aspas dentro da formatação.



""" n = 0
for pos, c in enumerate (times, start=1):
    print(f"{pos}, {times[n]}\n")
    n += 1
    if n == len(times):
        break
 """