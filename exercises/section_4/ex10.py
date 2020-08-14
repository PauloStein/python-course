"""
10 - Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s (metros por segundo).
A formula de conversao eh: M = K/3.6, sendo K a velocidade em km/h e M em m/s
"""

vel_km = float(input("digite a velocidade km/h"))
vel_ms = vel_km/3.6

print(f"A velocidade eh m/s eh: {vel_ms}")
