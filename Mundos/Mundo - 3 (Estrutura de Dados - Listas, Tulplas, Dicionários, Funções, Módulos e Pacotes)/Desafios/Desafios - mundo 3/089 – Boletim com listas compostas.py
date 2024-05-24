""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. """
temp = []
alunos = []
v  = 30
print('='*v)
print("Boletin Com Listas Compostas".center(v))


while True:
    print('='*v)
    print("[1] - Cadastrar aluno\n[2] - Mostrar Boletin\n[3] - Pesquisar Aluno \n[4] - Reprovados e Aprovados")
    print('='*v)
    opc = input("Opção: ")
    if opc.isdigit():
        opc = int(opc)

        print('='*v)
        if opc == 1:
            while True:
                print("Cadastro".center(v))
                print('='*v)
                nome = str(input("Nome: "))
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))
                temp = [nome, nota1, nota2]
                alunos.append(temp[:])
                temp.clear()
                print('='*v)

                ct = str(input("Quer continuar [S/N]:  ")).strip()
                print('='*v)
                if ct in 'Nn':
                    break

        if opc == 2:
            if len(alunos) == 0:
                print("Lista Vazia".center(v))
            else:
                print("Boletim".center(v))
                print('='*v)
                for index, c in enumerate(alunos, start=1):
                    print(f"{index}\nNome: {c[0]} \nNota1: {c[1]} \nNota2: {c[2]} \nMédia: {(c[1]+c[2]) / 2}")
                    print('='*v)

        if opc == 3:
            if len(alunos) == 0:
                print("Lista Vazia".center(v))
            else:
                print("Pesquisa".center(v))
                print('='*v)
                pesq = str(input("Nome do Aluno: ")).strip().capitalize()
                for index, c in enumerate(alunos, start=1):
                    if pesq == c[0]:
                        print(f"{index}\nNome: {c[0]} \nNota1: {c[1]} \nNota2: {c[2]} \nMédia: {(c[1]+c[2]) / 2}")
                        print('='*v)
        
        if opc == 4:
            print("[1] - Aprovados \n[2] - Reprovados")
            opc = int(input("Opção: "))
            if opc == 1:
                for index, c in enumerate(alunos, start=1):
                    cont = 0
                    if (c[1] + c[2] )/ 2 > 50:

                        print(f"{index}\nNome: {c[0]} \nNota1: {c[1]} \nNota2: {c[2]} \nMédia: {(c[1]+c[2]) / 2}")
                        cont += 1
                        print('='*v)
                        

            if opc == 2:
                for index, c in enumerate(alunos, start=1):
                    cont = 0
                    if (c[1] + c[2] )/ 2 < 50:
                        
                        print(f"{index}\nNome: {c[0]} \nNota1: {c[1]} \nNota2: {c[2]} \nMédia: {(c[1]+c[2]) / 2}")
                        cont +=1
                        if cont == len(alunos):
                            break
                        print('='*v)

        
        
        
        if opc == 5:
            print("Saindo . . .")
            print('='*v)
            break
    else:
        print("Valor Inválido!")    





