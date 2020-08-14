"""
10 - Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde H corresponde a altura):
homens: (72.7 * h) - 58
mulheres (62.1* h) - 44.7
"""

sexo= input("digite seu sexo (F ou M)")
altura= float(input("digite sua altura"))

if sexo == "M":
    peso_ideal= (72.7 * altura) - 58
    print(f"Peso ideal = {peso_ideal}")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal = {peso_ideal}")
else:
    print("digite um sexo valido")
