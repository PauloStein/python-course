"""
3 - Leia um numero fornecido pelo usuario. Se esse numero for positivo, calculo a raiz quadrada do numero. Do contrario, imprima o numero ao quadrado.
"""

numero = float(input("digite um numero"))

if numero >= 0:
    raiz = numero ** 0.5
    print(f"A raiz quadrada do numero eh: {raiz}")
else:
    quadrado = numero ** 2
    print(f"O numero ao quadrado eh: {quadrado}")

