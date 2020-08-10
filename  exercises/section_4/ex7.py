"""
7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius A formula de conversao eh:
C= 5.0 * (F-32.0) /9, sendo F a temperatura em Fahrenheit e C a temperatura em Celcius
"""

temperatura_fah = float(input("digite a temperatura em Fahrenheit"))
temperatura_celsius = 5.0 *(temperatura_fah-32)/9

print(f"temperatura em Celsius eh: {temperatura_celsius}")