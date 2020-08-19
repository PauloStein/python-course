"""
3 - Faca um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
iniciando em 10 e terminando em 0. Mostrar uma mensagem "Fim!" Apos a contagem
"""

x = 10
while x >= 0:
    print(x)
    if x == 0:
        print("FIM!")
    x -= 1
