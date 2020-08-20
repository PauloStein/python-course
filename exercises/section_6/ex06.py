"""
6 - Faca um programa que leia 10 valores inteiros e imprima sua media
"""

valor_dois = 0
for x in range(0, 10):
    valor = int(input("digite um valor"))
    x += 1
    valor_dois += valor

    if x == 10:
        print(f"valor = {valor_dois / x}")