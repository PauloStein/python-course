"""
6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit A formula de conversao eh:
F= c*(9.0/5.0) +32, sendo F a temperatura em Fahrenheit e C a temperatura em Celcius
"""

temperatura_celsius = float(input("digite a temperatura em celsius"))
temperatura_fah = temperatura_celsius *(9.0/5.0)+32

print(f"temperatura em Fahrenheit eh: {temperatura_fah}")