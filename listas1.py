# lista

# lista = [] vazia

pessoas = [
	'Fabio',
	'Matheus',
	'Mario',
	'Rodolfo',
	'Joao',
	'Thayana',
	'Andre'
]

print(type(pessoas))
print(len(pessoas))

# indices - acessar valores
print(pessoas[0])
print(pessoas[3])
print(pessoas[-1])
print(pessoas.index('Matheus'))

# fatias
print(pessoas[:3])
print(pessoas[0][0])

# alterar
pessoas[0] = 'Trump'
print(pessoas[0])

# adicionar - append  - adiciona no final
pessoas.append('Fabio')
print(pessoas)

# insert
pessoas.insert(0, 'Obama')
print(pessoas)

# print(id(pessoas[0]))
# print(id(pessoas[1]))
# print(id(pessoas))

# remover - pop - del - remove
pessoas.pop() #remove ultimo elemento
print(pessoas)

pessoas.remove('Joao')
print(pessoas)

del pessoas[2]
print(pessoas)

del pessoas[:]
print(pessoas)


# del pessoas
# print(pessoas)



