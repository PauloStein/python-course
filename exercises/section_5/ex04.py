"""
4 - Faca um programa que leia um numero e, caso ele seja positivo, calcule e mostre :
    - O numero digitado ao quadrado
    - A raiz quadrada do numero digitado
"""

numero = float(input("digite um numero"))

if numero >= 0:
    quadrado = numero ** 2
    print(f"O numero ao quadrado eh: {quadrado}")
    raiz = numero ** 0.5
    print(f"A raiz quadrada do numero eh: {raiz}")
else:
    print("Numero invalido")
