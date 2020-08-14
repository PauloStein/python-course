"""
7 - Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, se os numeros forem iguais, imprima a mensagem 'numeros iguais'
"""

n1 = int(input("digite um numero"))
n2 = int(input("digite outro numero"))

if n1 > n2:
    print(f"numero um eh maior {n1}")
elif n2 > n1:
    print(f"numero dois eh maior {n2}")
else:
    print('Os numeros sao iguais')