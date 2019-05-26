

# variaveis

lang = 'Python'

print(lang)
print(id(lang))
print(type(lang))  # string

ord = 1
print(type(ord))  # inteiro/int

ord2 = 2.0
print(type(ord2)) # float

ord3 = 2+3j
print(type(ord3)) # complex

numero = 1000.000000000
print('{:.1f}'.format(numero))

# variaveis compostas

listas = []
mercado = ['leite', 'pão','café', 'óleo', 'papel higienico']
print(mercado)

# indexar
print(mercado[0])
print(mercado[1])
print(mercado[2])
print(mercado[-1])

# fatias
print(mercado[1:])
print(mercado[2:])
print(mercado[2:4])

# alterar
mercado[0] = 'cerveja'
print(mercado)

# Adicionar
mercado.append('laranja')  # adiciona ao final da lista
print(mercado)

mercado.insert(0, 'Vinho')
print(mercado)

vegetais = ['cenoura', 'tomate', 'cebola']

mercado.extend(vegetais)
print(mercado)


print()
# clonar

mercado2 = mercado[:]
mercado[0]='queijo'
print(mercado2)
print(id(mercado2))
print()
print(mercado)
print(id(mercado))

m2 = mercado.copy()
print(m2)
print(id(m2))

# remover , pop, del, remove
print(mercado2)
mercado2.pop() # remove o ultimo elemento
print(mercado2)
mercado2.pop(0)  # indice
print(mercado2)

mercado2.remove('tomate')
print(mercado2)

del mercado2[0]
print(mercado2)

# mercado2 = []
# print(mercado2)

del mercado2[:]
print(mercado2)

# del mercado2
# print(mercado2)


print('-'*70)
#### Tuplas - () parenteses

shoppinglist = ('tennis', 'meias', 'cuecas', 'camisetas')
print(shoppinglist)
print(shoppinglist[0])
print(shoppinglist[-1])
print(shoppinglist[1:3])
print(id(shoppinglist))

shoppinglist2 = shoppinglist[1:2]
print(shoppinglist)
print(id(shoppinglist))

print('-'*70)
print(vegetais * 2)
dupla = shoppinglist * 2
print(id(dupla))
print(dupla)


print(shoppinglist + shoppinglist2)
print(mercado + vegetais)


