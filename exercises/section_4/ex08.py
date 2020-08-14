"""
8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius A formula de conversao eh:
C = K - 273.15, sendo C a temperatura em Celseius e K a temperatura em Kelvin
"""

temperatura_kel = float(input("digite a temperatura em Kelvin"))
temperatura_celsius = temperatura_kel - 273.15

print(f"temperatura em Celsius eh: {temperatura_celsius}")
