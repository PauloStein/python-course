# class Carro(object):
#     estado = "novo"
#     def dirigir(self):
#         self.estado = "usado"
#
#
# porsche = Carro()
# porsche.dirigir()
# print(porsche.estado)
#
# ferrari = Carro()
# print(ferrari.estado)

# class Carro(object):
#     def __init__(self, estado):
#         self.estado = estado
#
# bmw = Carro('semi-novo')
# print(bmw.estado)

class Veiculo(object):
    estado = "novo"

class Carro(Veiculo):
    pass


bmw = Carro()
print(bmw.estado)