"""
2 - Leia um numero fornecido pelo usuario. Se esse numero for positivo, calculo a raiz quadrada do numero. Se o numero for negativo mostre uma mensagem dizendo que o numero eh invalido.
"""

numero = float(input("digite um numero"))

if numero >= 0:
    raiz = numero ** 0.5
    print(f"A raiz quadrada do numero eh: {raiz}")
else:
    print("Numero invalido")
