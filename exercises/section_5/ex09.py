"""
9 - Leia o salario de um trabalhador e o valor da prestacao de um emprestimo. Se a prestacao for maior que 20% do
salario imprima: Emprestimo nao concedido, caso contrario imprima: Emprestimo concedido.
"""

salario = float(input("digite o salario"))
emprestimo = float(input("valor da prestacao do emprestimo"))

if emprestimo > salario * 0.2:
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")