"""
8 - Faca um programa que leia 2 notas de um aluno, verifique se as notas sao validas e exiba na tela a
media destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
onde caso a nota nao possua um valor valido, este fato deve ser informado ao usuario e o programa termina.
"""

nota1 = float(input("digite a nota um"))
nota2 = float(input("digite a nota dois"))

if nota1 < 0.0 or nota1 > 10.0:
    print("nota um invalida")
elif nota2 < 0.0 or nota2 > 10.0:
    print("nota dois invalida")
else:
    media = (nota1 + nota2) /2
    print(f"media = {media}")

