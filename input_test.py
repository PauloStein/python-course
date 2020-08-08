"""
Recebendo dado dos usuarios

input() tudo que eh recebido por input vira String
"""
# Data input
#print('Qual seu nome? ')
#nome = input()

nome = input('qual seu nome?')

#Exemplo de print da 2.x
#print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print da 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

#Exemplo de print 'mais atual 3.7>>'
print(f'Seja bem-vindo(a) {nome}')

#print('Qual sua idade? ')
#idade = input()

idade = input('Qual sua idade?')

# Processing

# Data output
#Exemplo de print da 2.x
#print('O %s tem %s anos ' % (nome,idade))

#Exemplo de print da 3.x
#print('O {0} tem {1} anos '.format(nome, idade))

#Exemplo de print 'mais atual 3.7>>'
print(f'O {nome} tem {idade} anos ')

"""
int(idade) = cast

Cast eh a 'conversao' de um tipo de dado para outro
"""

print(f'O {nome} nasceu em {2020 - int(idade)}')