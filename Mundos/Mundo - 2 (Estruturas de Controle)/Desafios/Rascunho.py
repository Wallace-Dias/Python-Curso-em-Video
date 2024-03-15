funcionario = ("Wallace", 22, "M")
for c in (funcionario):
    opc = str(input("[X] para excluír")).strip().upper()[0]
    if opc == 'X':
        del(funcionario)
    else:
        print("funcionário")
for c in range (0, 15):
    print(funcionario)









""" nomes = ('Wallace', 'Thamires', 'Luciana')
ct = 0
for c in range (0, len(nomes)):
for c in nomes:
for pos, c in enumerate (nomes):
    print(f"{pos}: {c}")
for cont in range(0, len(nomes)):
    print(f"{cont}: {nomes[cont]}")
    

        
print("Lista final") """