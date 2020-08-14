"""
6 - Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles assim como a diferenca existente entre ambos
"""

n1 = int(input("digite um numero"))
n2 = int(input("digite outro numero"))

if n1 > n2:
    print(f"numero um eh maior {n1}, a diferente entre n1 e n2 eh {n1 - n2}")
elif n2 > n1:
    print(f"numero dois eh maior {n2}, a diferente entre n1 e n2 eh {n2 - n1}")
else:
    print('Os numeros sao iguais')
