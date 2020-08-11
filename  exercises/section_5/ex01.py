"""
1 - Faca um programa que receba dois numeros qual deles eh maior
"""
n1 = int(input("digite um numero"))
n2 = int(input("digite outro numero"))

if n1 > n2:
    print("numero um maior que numero dois")
elif n2 > n1:
    print("numero dois maior que numero um")
else:
    print("os numeros sao iguais")
