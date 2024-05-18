
n = str(input("Digite algo: "))
lista = []

for i in n:
    if i == '(':
        lista.append('(')
        
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
            
        else:
            lista.append(')')
            break


if len(lista) == 0:
    print("Sua expressão é válida")
else:
    print("Expressão inválida")