
# nome = 'Fabio'
# sobrenome = 'Classo'
# # email = 'fabioclasso@email.com'
# email = nome + sobrenome +'@email.com'


# print(nome)
# print(sobrenome)
# print(email)

funcionarios = [
	['Fabio', 'Classo', 'email'],
	['Matheus', 'Furtado', 'email'],
]

# print(funcionarios)
# print(funcionarios[0])
# print(funcionarios[0][0])

nome = input('Digite nome:')
sobrenome = input('Digite sobrenome:')
email = input('Digite email:')

pessoa = nome + ", "+ sobrenome+ "," + email

funcionarios.append(pessoa)

arquivo = open('cadastropessoa.txt', 'w')
arquivo.write(str(funcionarios))

