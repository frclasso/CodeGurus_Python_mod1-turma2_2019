
# dicionarios = {key:value}

# mydic = {}  # dicionario vazio


empregado1 = {'nome':'Joanna',
              'sobrenome':'Silva',
              'idade':23,
              'pais':'Brazil'}


# Acessar valores
print(empregado1['nome'])
print(empregado1['sobrenome'])
print(empregado1['idade'])
print(empregado1['pais'])

# modificar
empregado1['pais'] = 'Brasil'
print(empregado1['pais'])

empregado1.update({'idade':22})
print(empregado1['idade'])

empregado1.update({'cidade':'Florianopolis'})
print(empregado1)

# deletar valores
del empregado1['idade']
print(empregado1)

print(type(empregado1))
print(id(empregado1))

# empregado1.clear()  # apaga todos os dados
# print(empregado1)

empregado2 = empregado1.copy()
print(empregado2)
print(id(empregado1))
print(id(empregado2))

empregado2.__delitem__('pais')
print(empregado2)

empregado2.pop('cidade')
print(empregado2)

del empregado2['sobrenome']
print(empregado2)

print(empregado1.keys())
print(empregado1.values())
print(empregado1.items())











