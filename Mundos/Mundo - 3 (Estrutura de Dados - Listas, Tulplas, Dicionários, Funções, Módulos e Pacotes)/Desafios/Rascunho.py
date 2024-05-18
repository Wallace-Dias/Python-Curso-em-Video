from time import sleep
n = str(input("Digite algo: "))
lista = []

for i in n:
    if i == '(':
        lista.append('(')
        
        print(f"Foi adicionado ( a lista e o valor é: {len(lista)}")
    elif i == ')':
        if len(lista) > 0:
            print(f" i foi == ) > 0 Len da Lista: {len(lista)}")
            lista.pop()
            print(f"ultimo item removio Len da Lista: {len(lista)}")
        else:
            lista.append(')')
            print(f"i == ) == 0 Len da Lista: {len(lista)}")
            break

print(f"Len final da lista: {len(lista)}")

if len(lista) == 0:
    print("Sua expressão é válida")
else:
    print("Expressão inválida")