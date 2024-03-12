""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. """

from time import sleep
print("="*30)
print(f"Tabuada".center(30))
print("="*30)
while True:
    n1 = int(input("Digite um número:".rjust(23)))
    if n1 < 0:
        break

    print("="*30)
    for c in range(1, 11):
        print(f"{n1} x {c} = {n1 * c}".center(30))
    print("="*30)

        

    

print("\nSaindo . . .")
sleep(2)
print("\nFinalizado!")







""" 
from time import sleep
print("="*30)
print(f"Tabuada".center(30))
print("="*30)
while True:
    n1 = int(input("Digite um número:".rjust(23)))
    if n1 < 0:
        break
    print("="*30)
    print(f"{n1} x {1} = {n1 * 1}".center(30))
    print(f"{n1} x {2} = {n1 * 2}".center(30))
    print(f"{n1} x {3} = {n1 * 3}".center(30))
    print(f"{n1} x {4} = {n1 * 4}".center(30))
    print(f"{n1} x {5} = {n1 * 5}".center(30))
    print(f"{n1} x {6} = {n1 * 6}".center(30))
    print(f"{n1} x {7} = {n1 * 7}".center(30))
    print(f"{n1} x {8} = {n1 * 8}".center(30))
    print(f"{n1} x {9} = {n1 * 9}".center(30))
    print(f"{n1} x {10} = {n1 * 10}".center(30))
    print("="*30)

    

print("\nSaindo . . .")
sleep(2)
print("\nFinalizado!")



"""