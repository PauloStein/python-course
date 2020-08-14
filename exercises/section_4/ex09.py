"""
9 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A formula de conversao eh:
K = C +273.15, sendo C a temperatura em Celseius e K a temperatura em Kelvin
"""

temperatura_celsius = float(input("digite a temperatura em Celsius"))
temperatura_kel = temperatura_celsius + 273.15

print(f"temperatura em Kelvin eh: {temperatura_kel}")
