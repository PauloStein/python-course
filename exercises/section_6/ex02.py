"""
2 - Escreva um programa que escreva na tela, de 1 ate 100, de 1 em 1, 3 vezes.
A primeira com for, a segunda com while e a terceira com do while
"""

for x in range(100):
    print(x+1)

x = 0
while x < 100:
    print(x+1)
    x += 1

x = 0
while True:
    print(x+1)
    x += 1
    if x == 100:
        break
