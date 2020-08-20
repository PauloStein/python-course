"""
5 - Faca um programa que peca ao usuario para digitar 10 valores e some-os
"""
valor_dois = 0
for x in range(0, 10):
    valor = int(input("digite um valor"))
    x += 1
    valor_dois += valor

    if x == 10:
        print(f"valor = {valor_dois}")